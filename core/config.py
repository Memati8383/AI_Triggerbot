"""
Configuration Manager
Handles all configuration loading, saving, and validation
"""
import json
import os
from typing import Dict, Any

class ConfigManager:
    """Manages application configuration"""
    
    DEFAULT_CONFIG = {
        # Detection settings
        'confidence': 0.20,
        'box_size': 400,
        'target_class': 0,
        
        # Aim settings
        'headshot_mode': True,
        'auto_aim': True,
        'aim_smooth': 0.5,
        'aim_tolerance': 40,
        'reaction_delay': 0.012,
        
        # Visual settings
        'show_window': True,
        'window_scale': 2.0,
        'show_heatmap': True,
        'show_trails': True,
        'show_performance': True,
        'fov_circle': True,
        'crosshair_style': 'cross',
        
        # Advanced features
        'track_targets': True,
        'prediction_enabled': True,
        'prediction_factor': 0.18,
        'anti_detection': True,
        'sound_alerts': False,
        'adaptive_confidence': True,
        
        # Combat settings
        'burst_mode': False,
        'burst_count': 3,
        'burst_delay': 0.08,
        'recoil_control': True,
        'recoil_pattern': [0, -2, -3, -4, -3, -2],
        
        # Target priority
        'target_priority': 'closest',
        'max_distance': 180,
        'min_target_size': 15,
        
        # Profile
        'profile': 'balanced',
        
        # Performance
        'target_fps': 120,
        'use_half_precision': False,
    }
    
    def __init__(self, config_file: str = 'config.json'):
        self.config_file = config_file
        self.config = self.DEFAULT_CONFIG.copy()
        self.load()
    
    def load(self) -> None:
        """Load configuration from file"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    self.config.update(loaded)
                print(f"[✓] Config loaded: {self.config_file}")
            except Exception as e:
                print(f"[!] Config load error: {e}")
        else:
            self.save()
    
    def save(self) -> None:
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)
            print(f"[✓] Config saved: {self.config_file}")
        except Exception as e:
            print(f"[!] Config save error: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value"""
        self.config[key] = value
    
    def update(self, updates: Dict[str, Any]) -> None:
        """Update multiple configuration values"""
        self.config.update(updates)
