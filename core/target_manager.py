"""
Target Management Module
Handles target prioritization and tracking
"""
import numpy as np
from typing import List, Optional, Tuple
from core.detector import Detection

class TargetManager:
    """Manages target selection and prioritization"""
    
    def __init__(self):
        self.last_target = None
    
    def prioritize(self, detections: List[Detection], 
                   screen_center: float,
                   priority_mode: str = 'closest',
                   max_distance: float = 180,
                   min_size: float = 15) -> Optional[Tuple]:
        """
        Prioritize targets based on criteria
        
        Args:
            detections: List of detections
            screen_center: Screen center position
            priority_mode: 'closest', 'highest_conf', or 'largest'
            max_distance: Maximum distance from center
            min_size: Minimum target size
            
        Returns:
            (detection, target_x, target_y, distance) or None
        """
        if not detections:
            return None
        
        scored_targets = []
        
        for det in detections:
            target_x, target_y = det.center
            
            # Calculate distance from center
            distance = np.sqrt(
                (target_x - screen_center)**2 + 
                (target_y - screen_center)**2
            )
            
            # Apply filters
            if distance > max_distance:
                continue
            if det.size < min_size:
                continue
            
            # Calculate score based on priority mode
            if priority_mode == 'closest':
                score = -distance  # Negative so closer = higher score
            elif priority_mode == 'highest_conf':
                score = det.confidence * 1000
            elif priority_mode == 'largest':
                score = det.size
            else:
                score = -distance
            
            scored_targets.append((det, target_x, target_y, distance, score))
        
        if not scored_targets:
            return None
        
        # Select best target
        best = max(scored_targets, key=lambda x: x[4])
        self.last_target = best[:4]  # Store without score
        
        return self.last_target
    
    def calculate_distance(self, x: float, y: float, 
                          center_x: float, center_y: float) -> float:
        """Calculate distance from center"""
        return np.sqrt((x - center_x)**2 + (y - center_y)**2)
    
    def is_in_tolerance(self, distance: float, tolerance: float) -> bool:
        """Check if target is within tolerance"""
        return distance <= tolerance
