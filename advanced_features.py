"""
Gelişmiş özellikler modülü
"""
import numpy as np
import cv2
from collections import deque
from time import time

class HeatmapTracker:
    """Hedef yoğunluk haritası"""
    def __init__(self, size=300):
        self.size = size
        self.heatmap = np.zeros((size, size), dtype=np.float32)
        self.decay_rate = 0.95
        
    def add_detection(self, x, y, confidence):
        """Tespit ekle"""
        x, y = int(x), int(y)
        if 0 <= x < self.size and 0 <= y < self.size:
            self.heatmap[y, x] += confidence * 10
            # Gaussian blur ile yay
            self.heatmap = cv2.GaussianBlur(self.heatmap, (15, 15), 0)
    
    def update(self):
        """Haritayı güncelle (decay)"""
        self.heatmap *= self.decay_rate
    
    def get_heatmap_overlay(self, frame):
        """Heatmap overlay oluştur"""
        # Normalize et
        normalized = cv2.normalize(self.heatmap, None, 0, 255, cv2.NORM_MINMAX)
        colored = cv2.applyColorMap(normalized.astype(np.uint8), cv2.COLORMAP_JET)
        
        # Frame ile birleştir
        overlay = cv2.addWeighted(frame, 0.7, colored, 0.3, 0)
        return overlay

class PerformanceMonitor:
    """Performans izleyici"""
    def __init__(self):
        self.frame_times = deque(maxlen=100)
        self.detection_times = deque(maxlen=100)
        self.aim_times = deque(maxlen=100)
        
    def record_frame_time(self, duration):
        self.frame_times.append(duration)
    
    def record_detection_time(self, duration):
        self.detection_times.append(duration)
    
    def record_aim_time(self, duration):
        self.aim_times.append(duration)
    
    def get_stats(self):
        """İstatistikleri al"""
        return {
            'avg_frame_time': np.mean(self.frame_times) if self.frame_times else 0,
            'avg_detection_time': np.mean(self.detection_times) if self.detection_times else 0,
            'avg_aim_time': np.mean(self.aim_times) if self.aim_times else 0,
            'fps': 1.0 / np.mean(self.frame_times) if self.frame_times and np.mean(self.frame_times) > 0 else 0,
        }

class TargetTracker:
    """Hedef takip sistemi"""
    def __init__(self, max_age=10):
        self.tracks = {}
        self.next_id = 0
        self.max_age = max_age
        
    def update(self, detections):
        """Tespitleri güncelle ve ID ata"""
        current_time = time()
        
        # Eski track'leri temizle
        self.tracks = {k: v for k, v in self.tracks.items() 
                      if current_time - v['last_seen'] < self.max_age}
        
        tracked_detections = []
        
        for det in detections:
            x1, y1, x2, y2, conf = det
            center = ((x1 + x2) / 2, (y1 + y2) / 2)
            
            # En yakın track'i bul
            best_match = None
            min_dist = float('inf')
            
            for track_id, track in self.tracks.items():
                dist = np.sqrt((center[0] - track['center'][0])**2 + 
                             (center[1] - track['center'][1])**2)
                if dist < min_dist and dist < 50:  # 50px threshold
                    min_dist = dist
                    best_match = track_id
            
            if best_match is not None:
                # Mevcut track'i güncelle
                self.tracks[best_match]['center'] = center
                self.tracks[best_match]['last_seen'] = current_time
                self.tracks[best_match]['hits'] += 1
                track_id = best_match
            else:
                # Yeni track oluştur
                track_id = self.next_id
                self.next_id += 1
                self.tracks[track_id] = {
                    'center': center,
                    'last_seen': current_time,
                    'hits': 1,
                    'first_seen': current_time
                }
            
            tracked_detections.append((det, track_id))
        
        return tracked_detections

class AimAssist:
    """Gelişmiş nişan yardımı"""
    def __init__(self):
        self.history = deque(maxlen=5)
        
    def calculate_lead(self, current_pos, velocity):
        """Lead hesapla (hareket eden hedef için)"""
        # Basit lead hesaplama
        lead_x = velocity[0] * 0.1
        lead_y = velocity[1] * 0.1
        return (current_pos[0] + lead_x, current_pos[1] + lead_y)
    
    def smooth_trajectory(self, target_pos):
        """Yumuşak yörünge"""
        self.history.append(target_pos)
        
        if len(self.history) < 2:
            return target_pos
        
        # Ortalama al
        avg_x = np.mean([p[0] for p in self.history])
        avg_y = np.mean([p[1] for p in self.history])
        
        return (avg_x, avg_y)

class SoundAlert:
    """Ses uyarı sistemi (basit beep)"""
    def __init__(self):
        self.last_alert = 0
        self.alert_cooldown = 0.5
        
    def play_detection_sound(self):
        """Tespit sesi"""
        current_time = time()
        if current_time - self.last_alert > self.alert_cooldown:
            # Windows beep (frekans, süre)
            try:
                import winsound
                winsound.Beep(1000, 100)
            except:
                pass
            self.last_alert = current_time
    
    def play_lock_sound(self):
        """Kilit sesi"""
        try:
            import winsound
            winsound.Beep(1500, 150)
        except:
            pass

class ProfileManager:
    """Profil yöneticisi"""
    def __init__(self):
        self.profiles = {
            'aggressive': {
                'confidence': 0.20,
                'aim_smooth': 0.6,
                'reaction_delay': 0.01,
                'burst_mode': True,
                'burst_count': 5,
            },
            'balanced': {
                'confidence': 0.25,
                'aim_smooth': 0.4,
                'reaction_delay': 0.02,
                'burst_mode': False,
            },
            'stealth': {
                'confidence': 0.35,
                'aim_smooth': 0.3,
                'reaction_delay': 0.05,
                'burst_mode': False,
            },
            'sniper': {
                'confidence': 0.40,
                'aim_smooth': 0.2,
                'reaction_delay': 0.03,
                'headshot_mode': True,
                'burst_mode': False,
            }
        }
    
    def get_profile(self, name):
        """Profil al"""
        return self.profiles.get(name, self.profiles['balanced'])
    
    def list_profiles(self):
        """Profilleri listele"""
        return list(self.profiles.keys())

class AntiDetection:
    """Anti-detection özellikleri"""
    def __init__(self):
        self.last_action = 0
        self.action_pattern = []
        
    def add_randomness(self, value, variance=0.1):
        """Rastgelelik ekle"""
        random_factor = np.random.uniform(1 - variance, 1 + variance)
        return value * random_factor
    
    def should_skip_shot(self, probability=0.05):
        """Bazen atışı atla (insan benzeri)"""
        return np.random.random() < probability
    
    def get_human_delay(self, base_delay):
        """İnsan benzeri gecikme"""
        # Gaussian dağılım ile rastgele gecikme
        return max(0.01, np.random.normal(base_delay, base_delay * 0.2))

class CrosshairOverlay:
    """Özel nişangah overlay"""
    def __init__(self):
        self.styles = {
            'cross': self._draw_cross,
            'dot': self._draw_dot,
            'circle': self._draw_circle,
            'square': self._draw_square,
        }
        self.current_style = 'cross'
    
    def draw(self, frame, center, color=(0, 255, 0), size=20):
        """Nişangah çiz"""
        return self.styles[self.current_style](frame, center, color, size)
    
    def _draw_cross(self, frame, center, color, size):
        cv2.line(frame, (center[0] - size, center[1]), 
                (center[0] + size, center[1]), color, 2)
        cv2.line(frame, (center[0], center[1] - size), 
                (center[0], center[1] + size), color, 2)
        return frame
    
    def _draw_dot(self, frame, center, color, size):
        cv2.circle(frame, center, size // 4, color, -1)
        return frame
    
    def _draw_circle(self, frame, center, color, size):
        cv2.circle(frame, center, size, color, 2)
        return frame
    
    def _draw_square(self, frame, center, color, size):
        cv2.rectangle(frame, 
                     (center[0] - size, center[1] - size),
                     (center[0] + size, center[1] + size),
                     color, 2)
        return frame
