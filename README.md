# 🎯 AI Triggerbot - Clean Architecture Edition

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![YOLO](https://img.shields.io/badge/YOLO-v11-green.svg)](https://github.com/ultralytics/ultralytics)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)](LICENSE)

Profesyonel, modüler ve yüksek performanslı AI triggerbot sistemi. YOLO11 + Clean Architecture.

![Demo](https://via.placeholder.com/800x400/1a1a1a/00ff00?text=AI+Triggerbot+Demo)

## ⚠️ Önemli Uyarı

**Bu proje sadece eğitim amaçlıdır.** Online oyunlarda kullanmayın. Anti-cheat sistemleri tespit edebilir. Etik kullanım sorumluluğu kullanıcıya aittir.

## ✨ Özellikler

```
AI_Triggerbot/
├── app.py                      # Ana uygulama
├── run.bat                     # Başlatma scripti
├── config.json                 # Konfigürasyon
├── requirements.txt            # Bağımlılıklar
│
├── core/                       # Çekirdek modüller
│   ├── __init__.py
│   ├── config.py              # Konfigürasyon yönetimi
│   ├── detector.py            # AI tespit motoru
│   ├── screen_capture.py     # Ekran yakalama
│   ├── aim_controller.py     # Nişan ve ateş kontrolü
│   └── target_manager.py     # Hedef yönetimi
│
├── ui/                        # Kullanıcı arayüzü
│   ├── __init__.py
│   └── visualizer.py         # Debug penceresi
│
├── utils/                     # Yardımcı araçlar
│   ├── __init__.py
│   ├── performance.py        # Performans izleme
│   └── input_handler.py      # Klavye girişi
│
├── advanced_features.py       # Gelişmiş özellikler
└── models/
    └── yolo11s.pt            # AI model
```

## ✨ Özellikler

### 🏗️ Clean Architecture
- **Modüler Yapı**: Her modül tek sorumluluk
- **Bağımsız Katmanlar**: Core, UI, Utils ayrımı
- **Kolay Test**: Her modül bağımsız test edilebilir
- **Genişletilebilir**: Yeni özellikler kolayca eklenir

### ⚡ Yüksek Performans
- **120 FPS Hedef**: Optimize edilmiş döngü
- **GPU Hızlandırma**: CUDA desteği
- **Verimli Bellek**: Minimal allocation
- **Akıllı Sleep**: FPS'e göre dinamik bekleme

### 🖼️ Gelişmiş Debug Penceresi
- **2x Büyük Pencere**: Daha iyi görünürlük
- **Canlı İstatistikler**: FPS, accuracy, detections
- **Performans Barları**: Görsel FPS göstergesi
- **Hedef İzleme**: Bounding box ve trails
- **Özelleştirilebilir**: Crosshair stilleri

### 🎯 AI Özellikleri
- **YOLO11 Model**: En son nesil tespit
- **Hedef Takibi**: ID sistemi
- **Hareket Tahmini**: Lead calculation
- **Akıllı Önceliklendirme**: Closest/Conf/Largest
- **Adaptif Confidence**: Otomatik ayarlama

## 🚀 Kurulum

```bash
# Virtual environment
python -m venv venv
.\venv\Scripts\activate

# Paketleri yükle
pip install torch torchvision ultralytics
pip install mss numpy pywin32 opencv-python

# Çalıştır
python app.py
# VEYA
run.bat
```

## 🎮 Kullanım

### Kontroller
| Tuş | Fonksiyon |
|-----|-----------|
| F2 | Aktif/Pasif |
| F3/F4 | Confidence ±0.05 |
| F5 | Hedef Önceliği |
| F6/F7 | Kaydet/Yükle |
| F8 | Panic Mode |
| F9 | Debug Penceresi |
| F10 | Profil Değiştir |
| F11 | Heatmap |
| F12 | Ses Uyarıları |

### Hızlı Başlangıç
1. `run.bat` ile başlat
2. F2 ile aktif et
3. F4 ile confidence'ı azalt (0.15-0.20)
4. Oyunu tam ekran aç
5. Nişangahı hedefe getir

## ⚙️ Konfigürasyon

### Performans Ayarları
```json
{
    "target_fps": 120,
    "box_size": 400,
    "window_scale": 2.0
}
```

### Tespit Ayarları
```json
{
    "confidence": 0.20,
    "target_priority": "closest",
    "max_distance": 180,
    "min_target_size": 15
}
```

### Nişan Ayarları
```json
{
    "headshot_mode": true,
    "auto_aim": true,
    "aim_smooth": 0.5,
    "aim_tolerance": 40,
    "reaction_delay": 0.012
}
```

## 📊 Performans

### Beklenen FPS
- **RTX 3060**: 100-120 FPS
- **RTX 3070**: 110-130 FPS
- **RTX 3080**: 120-140 FPS
- **RTX 4090**: 140-160 FPS

### Optimizasyon İpuçları
1. **GPU Kullan**: CUDA aktif olmalı
2. **Box Size**: 300-400 optimal
3. **Target FPS**: 120 önerilen
4. **Window Scale**: 2.0 performans/görünürlük dengesi
5. **Heatmap**: Kapatırsan +10 FPS

## 🏗️ Mimari Detayları

### Core Katmanı
- **config.py**: Tüm ayarları yönetir
- **detector.py**: YOLO model ve tespit
- **screen_capture.py**: Ekran yakalama
- **aim_controller.py**: Mouse ve ateş kontrolü
- **target_manager.py**: Hedef seçimi ve önceliklendirme

### UI Katmanı
- **visualizer.py**: Debug penceresi ve görselleştirme

### Utils Katmanı
- **performance.py**: FPS ve timing
- **input_handler.py**: Klavye girişi

### Veri Akışı
```
Screen → Capture → Detector → Target Manager → Aim Controller → Fire
                      ↓
                  Visualizer (Debug Window)
                      ↓
              Performance Monitor
```

## 🔧 Geliştirme

### Yeni Özellik Ekleme
1. İlgili modülü bul (core/ui/utils)
2. Yeni fonksiyon/class ekle
3. `__init__.py`'ye export et
4. `app.py`'de kullan

### Test
```python
# Modül testi
from core.detector import AIDetector
detector = AIDetector('models/yolo11s.pt')
```

### Debug
```python
# Performans profiling
from utils.performance import PerformanceMonitor
perf = PerformanceMonitor()
```

## 📝 Değişiklikler

### v5.0 (Clean Architecture)
- ✨ Tamamen modüler yapı
- ✨ Clean code prensipleri
- ✨ 120 FPS hedef
- ✨ 2x büyük debug penceresi
- ✨ Gelişmiş performans izleme
- ✨ Kolay genişletilebilir
- 🔧 Optimize edilmiş döngü
- 🔧 Verimli bellek kullanımı

## ⚠️ Notlar

- Sadece eğitim amaçlıdır
- Online oyunlarda kullanmayın
- Etik kullanım sorumluluğu kullanıcıya aittir

## 📄 Lisans

Eğitim amaçlıdır. Ticari kullanım yasaktır.

---

**🎯 Clean Architecture Edition - Profesyonel, Modüler, Hızlı!**
