"""
Screen Capture Module
Handles screen capturing with optimizations
"""
import numpy as np
import mss
from typing import Tuple

class ScreenCapture:
    """Optimized screen capture"""
    
    def __init__(self):
        self.sct = mss.mss()
        self.monitor = self.sct.monitors[1]
        self.screen_width = self.monitor['width']
        self.screen_height = self.monitor['height']
        self.center_x = self.screen_width // 2
        self.center_y = self.screen_height // 2
        
        print(f"[✓] Screen: {self.screen_width}x{self.screen_height}")
    
    def capture_region(self, box_size: int) -> np.ndarray:
        """
        Capture screen region around center
        
        Args:
            box_size: Size of capture box
            
        Returns:
            RGB image array
        """
        half_box = box_size // 2
        region = {
            'left': self.center_x - half_box,
            'top': self.center_y - half_box,
            'width': box_size,
            'height': box_size
        }
        
        screenshot = self.sct.grab(region)
        # Convert to RGB numpy array (remove alpha channel)
        return np.array(screenshot)[:, :, :3]
    
    def get_screen_info(self) -> dict:
        """Get screen information"""
        return {
            'width': self.screen_width,
            'height': self.screen_height,
            'center': (self.center_x, self.center_y)
        }
