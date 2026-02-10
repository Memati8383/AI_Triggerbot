"""
Performance Monitoring Module
Tracks FPS and timing metrics
"""
from time import time
from collections import deque
from typing import Dict

class PerformanceMonitor:
    """Monitors application performance"""
    
    def __init__(self, history_size: int = 120):
        self.frame_times = deque(maxlen=history_size)
        self.detection_times = deque(maxlen=history_size)
        self.render_times = deque(maxlen=history_size)
        self.last_frame_time = time()
    
    def start_frame(self) -> float:
        """Start frame timing"""
        return time()
    
    def end_frame(self, start_time: float) -> None:
        """End frame timing"""
        frame_time = time() - start_time
        self.frame_times.append(frame_time)
    
    def record_detection(self, duration: float) -> None:
        """Record detection time"""
        self.detection_times.append(duration)
    
    def record_render(self, duration: float) -> None:
        """Record render time"""
        self.render_times.append(duration)
    
    def get_fps(self) -> float:
        """Get current FPS"""
        if not self.frame_times:
            return 0.0
        
        avg_time = sum(self.frame_times) / len(self.frame_times)
        return 1.0 / avg_time if avg_time > 0 else 0.0
    
    def get_stats(self) -> Dict[str, float]:
        """Get performance statistics"""
        return {
            'fps': self.get_fps(),
            'avg_frame_time': sum(self.frame_times) / len(self.frame_times) if self.frame_times else 0,
            'avg_detection_time': sum(self.detection_times) / len(self.detection_times) if self.detection_times else 0,
            'avg_render_time': sum(self.render_times) / len(self.render_times) if self.render_times else 0,
        }
    
    def calculate_sleep_time(self, target_fps: int) -> float:
        """Calculate sleep time to maintain target FPS"""
        if not self.frame_times:
            return 1.0 / target_fps
        
        target_time = 1.0 / target_fps
        actual_time = self.frame_times[-1]
        
        return max(0, target_time - actual_time)
