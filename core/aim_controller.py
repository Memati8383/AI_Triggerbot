"""
Aim Controller Module
Handles aiming, shooting, and recoil control
"""
import win32api
import win32con
from time import sleep
from typing import Tuple
from collections import deque

class AimController:
    """Controls mouse movement and shooting"""
    
    def __init__(self):
        self.shot_count = 0
        self.position_history = deque(maxlen=5)
    
    def move_mouse(self, dx: int, dy: int) -> None:
        """
        Move mouse by delta
        
        Args:
            dx: X delta
            dy: Y delta
        """
        if abs(dx) > 1 or abs(dy) > 1:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
    
    def smooth_aim(self, target_x: float, target_y: float, 
                   screen_center: float, smoothness: float) -> Tuple[int, int]:
        """
        Calculate smooth aim movement
        
        Args:
            target_x: Target X position
            target_y: Target Y position
            screen_center: Screen center position
            smoothness: Smoothness factor (0-1)
            
        Returns:
            (dx, dy) movement deltas
        """
        dx = target_x - screen_center
        dy = target_y - screen_center
        
        smooth_dx = int(dx * smoothness)
        smooth_dy = int(dy * smoothness)
        
        return smooth_dx, smooth_dy
    
    def fire(self, delay: float = 0.05) -> None:
        """
        Fire weapon
        
        Args:
            delay: Delay before firing
        """
        sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        self.shot_count += 1
    
    def burst_fire(self, count: int, delay: float, 
                   recoil_pattern: list = None) -> None:
        """
        Fire burst
        
        Args:
            count: Number of shots
            delay: Delay between shots
            recoil_pattern: Recoil compensation pattern
        """
        for i in range(count):
            # Apply recoil compensation
            if recoil_pattern and i < len(recoil_pattern):
                recoil_y = recoil_pattern[i]
                if recoil_y != 0:
                    self.move_mouse(0, recoil_y)
            
            self.fire(0.01)
            
            if i < count - 1:
                sleep(delay)
    
    def calculate_target_point(self, x1: float, y1: float, 
                               x2: float, y2: float, 
                               headshot_mode: bool = True) -> Tuple[float, float]:
        """
        Calculate optimal target point
        
        Args:
            x1, y1, x2, y2: Bounding box coordinates
            headshot_mode: Target head or center
            
        Returns:
            (target_x, target_y)
        """
        width = x2 - x1
        height = y2 - y1
        
        target_x = (x1 + x2) / 2
        
        if headshot_mode:
            # Target upper 20% (head area)
            target_y = y1 + height * 0.2
        else:
            # Target center 40% (chest area)
            target_y = y1 + height * 0.4
        
        return target_x, target_y
    
    def predict_movement(self, current_pos: Tuple[float, float], 
                        prediction_factor: float = 0.15) -> Tuple[float, float]:
        """
        Predict target movement
        
        Args:
            current_pos: Current position
            prediction_factor: Prediction strength
            
        Returns:
            Predicted position
        """
        self.position_history.append(current_pos)
        
        if len(self.position_history) < 3:
            return current_pos
        
        # Calculate velocity from last 3 positions
        positions = list(self.position_history)[-3:]
        dx = positions[-1][0] - positions[0][0]
        dy = positions[-1][1] - positions[0][1]
        
        # Predict future position
        pred_x = current_pos[0] + dx * prediction_factor
        pred_y = current_pos[1] + dy * prediction_factor
        
        return pred_x, pred_y
    
    def reset_stats(self) -> None:
        """Reset statistics"""
        self.shot_count = 0
        self.position_history.clear()
