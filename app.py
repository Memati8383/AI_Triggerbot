"""
AI Triggerbot - Clean Architecture Edition
Main application entry point
"""
import sys
from time import sleep
import threading

# Core modules
from core.config import ConfigManager
from core.detector import AIDetector
from core.screen_capture import ScreenCapture
from core.aim_controller import AimController
from core.target_manager import TargetManager

# UI modules
from ui.visualizer import Visualizer

# Utils
from utils.performance import PerformanceMonitor
from utils.input_handler import InputHandler, HotkeyManager

# Advanced features
from advanced_features import (
    HeatmapTracker, TargetTracker, SoundAlert,
    ProfileManager, AntiDetection
)

class TriggerBot:
    """Main triggerbot application"""
    
    def __init__(self):
        print("\n" + "="*70)
        print("🎯 AI TRIGGERBOT - CLEAN ARCHITECTURE EDITION")
        print("="*70 + "\n")
        
        # Initialize components
        self.config = ConfigManager()
        self.detector = AIDetector('models/yolo11s.pt', 
                                   self.config.get('target_class', 0))
        self.screen = ScreenCapture()
        self.aim = AimController()
        self.target_mgr = TargetManager()
        self.visualizer = Visualizer()
        self.perf_mon = PerformanceMonitor(history_size=120)
        self.input_handler = InputHandler()
        
        # Advanced features
        self.heatmap = HeatmapTracker(self.config.get('box_size', 400))
        self.tracker = TargetTracker()
        self.sound = SoundAlert()
        self.profiles = ProfileManager()
        self.anti_det = AntiDetection()
        
        # State
        self.active = False
        self.panic_mode = False
        self.running = True
        
        # Statistics
        self.detection_count = 0
        self.hit_count = 0
        self.miss_count = 0
        
        # Locks
        self.frame_lock = threading.Lock()
        self.current_frame = None
        self.current_detections = []
        
        print("[✓] All systems initialized")
        self._print_controls()
    
    def _print_controls(self) -> None:
        """Print control scheme"""
        print("\n[CONTROLS]")
        print("  F2  → Toggle On/Off")
        print("  F3  → Confidence +0.05")
        print("  F4  → Confidence -0.05")
        print("  F5  → Cycle Priority")
        print("  F6  → Save Config")
        print("  F7  → Load Config")
        print("  F8  → PANIC MODE")
        print("  F9  → Toggle Window")
        print("  F10 → Cycle Profile")
        print("  F11 → Toggle Heatmap")
        print("  F12 → Toggle Sound")
        print("="*70 + "\n")
    
    def process_frame(self) -> None:
        """Process single frame"""
        frame_start = self.perf_mon.start_frame()
        
        # Capture screen
        frame = self.screen.capture_region(self.config.get('box_size', 400))
        
        with self.frame_lock:
            self.current_frame = frame.copy()
        
        # Detect targets
        detect_start = self.perf_mon.start_frame()
        detections = self.detector.detect(
            frame, 
            self.config.get('confidence', 0.20)
        )
        self.perf_mon.record_detection(self.perf_mon.start_frame() - detect_start)
        
        # Track targets
        if self.config.get('track_targets', True):
            tracked = self.tracker.update([d.to_tuple() for d in detections])
            with self.frame_lock:
                self.current_detections = tracked
        else:
            with self.frame_lock:
                self.current_detections = [(d.to_tuple(), 0) for d in detections]
        
        if not detections:
            self.miss_count += 1
            self.heatmap.update()
            self.perf_mon.end_frame(frame_start)
            return
        
        # Sound alert
        if self.config.get('sound_alerts', False):
            self.sound.play_detection_sound()
        
        # Prioritize target
        box_size = self.config.get('box_size', 400)
        screen_center = box_size / 2
        
        target_data = self.target_mgr.prioritize(
            detections,
            screen_center,
            self.config.get('target_priority', 'closest'),
            self.config.get('max_distance', 180),
            self.config.get('min_target_size', 15)
        )
        
        if not target_data:
            self.miss_count += 1
            self.heatmap.update()
            self.perf_mon.end_frame(frame_start)
            return
        
        detection, target_x, target_y, distance = target_data
        
        # Calculate target point
        target_x, target_y = self.aim.calculate_target_point(
            detection.x1, detection.y1, detection.x2, detection.y2,
            self.config.get('headshot_mode', True)
        )
        
        # Movement prediction
        if self.config.get('prediction_enabled', True):
            target_x, target_y = self.aim.predict_movement(
                (target_x, target_y),
                self.config.get('prediction_factor', 0.18)
            )
        
        # Update heatmap
        if self.config.get('show_heatmap', True):
            self.heatmap.add_detection(target_x, target_y, detection.confidence)
        
        # Check if in tolerance
        if not self.target_mgr.is_in_tolerance(distance, 
                                               self.config.get('aim_tolerance', 40)):
            # Aim towards target
            if self.config.get('auto_aim', True):
                dx, dy = self.aim.smooth_aim(
                    target_x, target_y, screen_center,
                    self.config.get('aim_smooth', 0.5)
                )
                
                # Anti-detection randomness
                if self.config.get('anti_detection', True):
                    dx = int(self.anti_det.add_randomness(dx, 0.05))
                    dy = int(self.anti_det.add_randomness(dy, 0.05))
                
                self.aim.move_mouse(dx, dy)
            
            self.miss_count += 1
            self.heatmap.update()
            self.perf_mon.end_frame(frame_start)
            return
        
        # Anti-detection: skip shot sometimes
        if self.config.get('anti_detection', True):
            if self.anti_det.should_skip_shot(0.03):
                self.heatmap.update()
                self.perf_mon.end_frame(frame_start)
                return
        
        # Target locked - FIRE!
        self.detection_count += 1
        print(f"[{self.detection_count}] 🎯 LOCKED | "
              f"Conf:{detection.confidence:.2f} | Dist:{distance:.0f}px")
        
        if self.config.get('sound_alerts', False):
            self.sound.play_lock_sound()
        
        # Fire weapon
        if self.config.get('burst_mode', False):
            print(f"     💥💥💥 BURST!")
            self.aim.burst_fire(
                self.config.get('burst_count', 3),
                self.config.get('burst_delay', 0.08),
                self.config.get('recoil_pattern', [])
            )
        else:
            print(f"     💥 FIRE!")
            delay = self.config.get('reaction_delay', 0.012)
            if self.config.get('anti_detection', True):
                delay = self.anti_det.get_human_delay(delay)
            self.aim.fire(delay)
        
        self.hit_count += 1
        self.heatmap.update()
        self.perf_mon.end_frame(frame_start)
    
    def visual_thread(self) -> None:
        """Visual debug thread"""
        print("[✓] Visual thread started\n")
        
        while self.running:
            if not self.config.get('show_window', True):
                sleep(0.1)
                continue
            
            with self.frame_lock:
                if self.current_frame is not None:
                    try:
                        # Prepare stats
                        total_shots = self.aim.shot_count
                        accuracy = (self.hit_count / total_shots * 100) if total_shots > 0 else 0
                        
                        stats = {
                            'active': self.active,
                            'fps': self.perf_mon.get_fps(),
                            'target_fps': self.config.get('target_fps', 120),
                            'detection_count': self.detection_count,
                            'shot_count': total_shots,
                            'accuracy': accuracy,
                        }
                        
                        # Draw frame
                        display = self.visualizer.draw_frame(
                            self.current_frame,
                            [d[0] for d in self.current_detections],
                            stats,
                            self.config.config
                        )
                        
                        # Show
                        key = self.visualizer.show(
                            display, 
                            self.config.get('window_scale', 2.0)
                        )
                        
                        if key == 27 or key == ord('q'):
                            self.config.set('show_window', False)
                    
                    except Exception as e:
                        print(f"[!] Visual error: {e}")
            
            sleep(0.01)
    
    def handle_input(self) -> None:
        """Handle keyboard input"""
        # F2 - Toggle
        if self.input_handler.is_key_pressed(HotkeyManager.get_key('F2')):
            self.active = not self.active
            self.panic_mode = False
            status = "🟢 ACTIVE" if self.active else "🔴 INACTIVE"
            print(f"\n{'='*70}")
            print(f"Status: {status}")
            print(f"{'='*70}\n")
        
        # F3/F4 - Confidence
        if self.input_handler.is_key_pressed(HotkeyManager.get_key('F3')):
            conf = min(0.95, self.config.get('confidence') + 0.05)
            self.config.set('confidence', conf)
            print(f"[⬆] Confidence: {conf:.2f}")
        
        if self.input_handler.is_key_pressed(HotkeyManager.get_key('F4')):
            conf = max(0.10, self.config.get('confidence') - 0.05)
            self.config.set('confidence', conf)
            print(f"[⬇] Confidence: {conf:.2f}")
        
        # F5 - Priority
        if self.input_handler.is_key_pressed(HotkeyManager.get_key('F5')):
            priorities = ['closest', 'highest_conf', 'largest']
            current = self.config.get('target_priority')
            idx = priorities.index(current) if current in priorities else 0
            new_priority = priorities[(idx + 1) % len(priorities)]
            self.config.set('target_priority', new_priority)
            print(f"[🔄] Priority: {new_priority}")
        
        # F6/F7 - Save/Load
        if self.input_handler.is_key_pressed(HotkeyManager.get_key('F6')):
            self.config.save()
        
        if self.input_handler.is_key_pressed(HotkeyManager.get_key('F7')):
            self.config.load()
        
        # F8 - PANIC
        if self.input_handler.is_key_pressed(HotkeyManager.get_key('F8')):
            self.panic_mode = True
            self.active = False
            print(f"\n{'='*70}")
            print(f"[!!!] 🚨 PANIC MODE 🚨")
            print(f"{'='*70}\n")
        
        # F9 - Window
        if self.input_handler.is_key_pressed(HotkeyManager.get_key('F9')):
            show = not self.config.get('show_window', True)
            self.config.set('show_window', show)
            print(f"[👁] Window: {'ON' if show else 'OFF'}")
        
        # F10 - Profile
        if self.input_handler.is_key_pressed(HotkeyManager.get_key('F10')):
            profile_list = self.profiles.list_profiles()
            current = self.config.get('profile', 'balanced')
            idx = profile_list.index(current) if current in profile_list else 0
            new_profile = profile_list[(idx + 1) % len(profile_list)]
            
            profile_settings = self.profiles.get_profile(new_profile)
            self.config.update(profile_settings)
            self.config.set('profile', new_profile)
            print(f"[🔄] Profile: {new_profile.upper()}")
        
        # F11 - Heatmap
        if self.input_handler.is_key_pressed(HotkeyManager.get_key('F11')):
            show = not self.config.get('show_heatmap', True)
            self.config.set('show_heatmap', show)
            print(f"[🗺] Heatmap: {'ON' if show else 'OFF'}")
        
        # F12 - Sound
        if self.input_handler.is_key_pressed(HotkeyManager.get_key('F12')):
            sound = not self.config.get('sound_alerts', False)
            self.config.set('sound_alerts', sound)
            print(f"[🔊] Sound: {'ON' if sound else 'OFF'}")
    
    def run(self) -> None:
        """Main application loop"""
        print("[✓] Application running...\n")
        
        # Start visual thread
        if self.config.get('show_window', True):
            threading.Thread(target=self.visual_thread, daemon=True).start()
            sleep(0.5)
        
        try:
            while self.running:
                if self.panic_mode:
                    sleep(1)
                    continue
                
                # Handle input
                self.handle_input()
                
                # Process frame if active
                if self.active:
                    self.process_frame()
                    
                    # Sleep to maintain target FPS
                    sleep_time = self.perf_mon.calculate_sleep_time(
                        self.config.get('target_fps', 120)
                    )
                    sleep(sleep_time)
                else:
                    sleep(0.05)
        
        except KeyboardInterrupt:
            print("\n[!] Shutting down...")
        
        finally:
            self.shutdown()
    
    def shutdown(self) -> None:
        """Cleanup and shutdown"""
        self.running = False
        self.visualizer.close()
        
        # Print final stats
        total_shots = self.aim.shot_count
        accuracy = (self.hit_count / total_shots * 100) if total_shots > 0 else 0
        
        print("\n" + "="*70)
        print("📊 FINAL STATISTICS")
        print("="*70)
        print(f"  Detections: {self.detection_count}")
        print(f"  Shots: {total_shots}")
        print(f"  Hits: {self.hit_count}")
        print(f"  Accuracy: {accuracy:.1f}%")
        print(f"  Avg FPS: {self.perf_mon.get_fps():.1f}")
        print("="*70)
        print("✓ Goodbye!\n")

def main():
    """Application entry point"""
    try:
        app = TriggerBot()
        app.run()
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
