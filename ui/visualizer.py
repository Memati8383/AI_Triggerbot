"""
Visualization Module
Handles debug window and visual feedback
"""
import cv2
import numpy as np
from typing import List, Tuple, Optional
from collections import deque

class Visualizer:
    """Handles visual debug window"""
    
    def __init__(self, window_name: str = "AI Triggerbot - Pro"):
        self.window_name = window_name
        self.fps_history = deque(maxlen=60)
        self.heatmap = None
        
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        print(f"[✓] Debug window initialized")
    
    def draw_frame(self, frame: np.ndarray, 
                   detections: List,
                   stats: dict,
                   config: dict) -> np.ndarray:
        """
        Draw debug information on frame
        
        Args:
            frame: Input frame (RGB)
            detections: List of detections
            stats: Statistics dictionary
            config: Configuration dictionary
            
        Returns:
            Annotated frame (BGR for OpenCV)
        """
        # Convert RGB to BGR
        display = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        h, w = display.shape[:2]
        center = (w // 2, h // 2)
        
        # Draw FOV circle
        if config.get('fov_circle', True):
            tolerance = config.get('aim_tolerance', 40)
            cv2.circle(display, center, tolerance, (0, 255, 255), 3)
        
        # Draw crosshair
        self._draw_crosshair(display, center, config.get('crosshair_style', 'cross'))
        
        # Draw detections
        for det in detections:
            if hasattr(det, 'to_tuple'):
                x1, y1, x2, y2, conf = det.to_tuple()
            else:
                x1, y1, x2, y2, conf = det
            
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            
            # Bounding box
            cv2.rectangle(display, (x1, y1), (x2, y2), (0, 255, 0), 3)
            
            # Confidence label
            label = f"{conf:.2f}"
            cv2.putText(display, label, (x1, y1 - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            # Target point
            target_x = int((x1 + x2) / 2)
            if config.get('headshot_mode', True):
                target_y = int(y1 + (y2 - y1) * 0.2)
            else:
                target_y = int(y1 + (y2 - y1) * 0.4)
            
            cv2.circle(display, (target_x, target_y), 8, (0, 0, 255), -1)
            
            # Trail line
            if config.get('show_trails', True):
                cv2.line(display, center, (target_x, target_y), 
                        (255, 255, 0), 2)
        
        # Draw stats
        self._draw_stats(display, stats, config)
        
        # Draw performance bars
        if config.get('show_performance', True):
            self._draw_performance_bars(display, stats)
        
        return display
    
    def _draw_crosshair(self, frame: np.ndarray, center: Tuple[int, int], 
                       style: str = 'cross') -> None:
        """Draw crosshair"""
        size = 25
        color = (0, 255, 0)
        thickness = 3
        
        if style == 'cross':
            cv2.line(frame, (center[0] - size, center[1]), 
                    (center[0] + size, center[1]), color, thickness)
            cv2.line(frame, (center[0], center[1] - size), 
                    (center[0], center[1] + size), color, thickness)
        elif style == 'dot':
            cv2.circle(frame, center, size // 3, color, -1)
        elif style == 'circle':
            cv2.circle(frame, center, size, color, thickness)
        elif style == 'square':
            cv2.rectangle(frame, 
                         (center[0] - size, center[1] - size),
                         (center[0] + size, center[1] + size),
                         color, thickness)
    
    def _draw_stats(self, frame: np.ndarray, stats: dict, config: dict) -> None:
        """Draw statistics"""
        h, w = frame.shape[:2]
        y = 40
        
        # Status
        status = "ACTIVE" if stats.get('active', False) else "INACTIVE"
        color = (0, 255, 0) if stats.get('active', False) else (0, 0, 255)
        cv2.putText(frame, f"Status: {status}", (15, y),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        y += 35
        
        # Stats
        stat_lines = [
            f"FPS: {stats.get('fps', 0):.1f}",
            f"Conf: {config.get('confidence', 0):.2f}",
            f"Priority: {config.get('target_priority', 'closest')}",
            f"Detections: {stats.get('detection_count', 0)}",
            f"Shots: {stats.get('shot_count', 0)}",
            f"Accuracy: {stats.get('accuracy', 0):.1f}%",
        ]
        
        for line in stat_lines:
            cv2.putText(frame, line, (15, y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            y += 32
        
        # Active features
        features = []
        if config.get('headshot_mode', False):
            features.append("HEADSHOT")
        if config.get('auto_aim', False):
            features.append("AUTO-AIM")
        if config.get('prediction_enabled', False):
            features.append("PREDICT")
        if config.get('anti_detection', False):
            features.append("ANTI-DET")
        
        if features:
            feature_text = " | ".join(features)
            cv2.putText(frame, feature_text, (15, h - 25),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    
    def _draw_performance_bars(self, frame: np.ndarray, stats: dict) -> None:
        """Draw performance bars"""
        h, w = frame.shape[:2]
        bar_width = 250
        bar_height = 15
        bar_x = w - bar_width - 20
        bar_y = 20
        
        # FPS bar
        fps = stats.get('fps', 0)
        target_fps = stats.get('target_fps', 120)
        fps_ratio = min(fps / target_fps, 1.0)
        
        # Color based on performance
        if fps_ratio > 0.8:
            color = (0, 255, 0)
        elif fps_ratio > 0.5:
            color = (0, 255, 255)
        else:
            color = (0, 0, 255)
        
        # Background
        cv2.rectangle(frame, (bar_x, bar_y), 
                     (bar_x + bar_width, bar_y + bar_height), 
                     (50, 50, 50), -1)
        
        # Fill
        fill_width = int(bar_width * fps_ratio)
        cv2.rectangle(frame, (bar_x, bar_y), 
                     (bar_x + fill_width, bar_y + bar_height), 
                     color, -1)
        
        # Label
        cv2.putText(frame, f"FPS: {fps:.0f}/{target_fps}", 
                   (bar_x - 120, bar_y + 12),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    def show(self, frame: np.ndarray, scale: float = 2.0) -> int:
        """
        Show frame in window
        
        Args:
            frame: Frame to display
            scale: Scale factor
            
        Returns:
            Key pressed (or -1)
        """
        h, w = frame.shape[:2]
        new_w = int(w * scale)
        new_h = int(h * scale)
        resized = cv2.resize(frame, (new_w, new_h))
        
        cv2.imshow(self.window_name, resized)
        return cv2.waitKey(1) & 0xFF
    
    def close(self) -> None:
        """Close window"""
        cv2.destroyAllWindows()
