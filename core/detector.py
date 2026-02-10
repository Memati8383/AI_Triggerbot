"""
AI Detection Module
Handles YOLO model and object detection
"""
import torch
import numpy as np
from ultralytics import YOLO
from typing import List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Detection:
    """Detection data class"""
    x1: float
    y1: float
    x2: float
    y2: float
    confidence: float
    class_id: int = 0
    
    @property
    def center(self) -> Tuple[float, float]:
        """Get center point"""
        return ((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
    
    @property
    def size(self) -> float:
        """Get bounding box size"""
        return (self.x2 - self.x1) * (self.y2 - self.y1)
    
    def to_tuple(self) -> Tuple[float, float, float, float, float]:
        """Convert to tuple format"""
        return (self.x1, self.y1, self.x2, self.y2, self.confidence)

class AIDetector:
    """AI-powered object detector"""
    
    def __init__(self, model_path: str, target_class: int = 0):
        self.model_path = model_path
        self.target_class = target_class
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        
        print(f"[...] Loading AI model: {model_path}")
        self.model = YOLO(model_path)
        self.model.to(self.device)
        self.model.fuse()  # Optimize model
        
        print(f"[✓] Model loaded - Device: {self.device.upper()}")
        
        if self.device == 'cuda':
            print(f"[✓] GPU: {torch.cuda.get_device_name(0)}")
    
    def detect(self, frame: np.ndarray, confidence: float = 0.25) -> List[Detection]:
        """
        Detect objects in frame
        
        Args:
            frame: Input image (RGB format)
            confidence: Confidence threshold
            
        Returns:
            List of Detection objects
        """
        results = self.model(frame, verbose=False, conf=confidence)
        
        detections = []
        for result in results:
            if result.boxes is None:
                continue
            
            for box in result.boxes:
                class_id = int(box.cls[0])
                
                # Filter by target class
                if class_id != self.target_class:
                    continue
                
                conf = float(box.conf[0])
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                
                detection = Detection(
                    x1=x1, y1=y1, x2=x2, y2=y2,
                    confidence=conf, class_id=class_id
                )
                detections.append(detection)
        
        return detections
    
    def get_device_info(self) -> dict:
        """Get device information"""
        info = {'device': self.device}
        
        if self.device == 'cuda':
            info['gpu_name'] = torch.cuda.get_device_name(0)
            info['vram_total'] = torch.cuda.get_device_properties(0).total_memory / 1024**3
            info['vram_allocated'] = torch.cuda.memory_allocated(0) / 1024**3
        
        return info
