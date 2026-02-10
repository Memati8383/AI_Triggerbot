"""
Input Handler Module
Handles keyboard input and hotkeys
"""
import win32api
import win32con
from time import sleep
from typing import Callable, Dict

class InputHandler:
    """Handles keyboard input"""
    
    def __init__(self):
        self.key_cooldowns = {}
        self.cooldown_time = 0.25
    
    def is_key_pressed(self, vk_code: int, cooldown: bool = True) -> bool:
        """
        Check if key is pressed
        
        Args:
            vk_code: Virtual key code
            cooldown: Apply cooldown to prevent spam
            
        Returns:
            True if key is pressed
        """
        if win32api.GetAsyncKeyState(vk_code) & 0x8000:
            if cooldown:
                # Check cooldown
                if vk_code in self.key_cooldowns:
                    return False
                
                self.key_cooldowns[vk_code] = True
                return True
            return True
        else:
            # Reset cooldown when key released
            if vk_code in self.key_cooldowns:
                del self.key_cooldowns[vk_code]
            return False
    
    def handle_hotkeys(self, hotkey_map: Dict[int, Callable]) -> None:
        """
        Handle multiple hotkeys
        
        Args:
            hotkey_map: Dictionary of {vk_code: callback}
        """
        for vk_code, callback in hotkey_map.items():
            if self.is_key_pressed(vk_code):
                callback()
                sleep(self.cooldown_time)

class HotkeyManager:
    """Manages application hotkeys"""
    
    KEYS = {
        'F1': win32con.VK_F1,
        'F2': win32con.VK_F2,
        'F3': win32con.VK_F3,
        'F4': win32con.VK_F4,
        'F5': win32con.VK_F5,
        'F6': win32con.VK_F6,
        'F7': win32con.VK_F7,
        'F8': win32con.VK_F8,
        'F9': win32con.VK_F9,
        'F10': win32con.VK_F10,
        'F11': win32con.VK_F11,
        'F12': win32con.VK_F12,
    }
    
    @staticmethod
    def get_key(name: str) -> int:
        """Get virtual key code by name"""
        return HotkeyManager.KEYS.get(name, 0)
