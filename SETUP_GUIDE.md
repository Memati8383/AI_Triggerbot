# 🚀 Kurulum Rehberi

## Sistem Gereksinimleri

### Minimum
- **OS**: Windows 10/11
- **Python**: 3.11+
- **RAM**: 8 GB
- **GPU**: NVIDIA GTX 1060 (4GB VRAM)
- **Disk**: 5 GB boş alan

### Önerilen
- **OS**: Windows 11
- **Python**: 3.11
- **RAM**: 16 GB
- **GPU**: NVIDIA RTX 3060+ (6GB+ VRAM)
- **Disk**: 10 GB boş alan

## Adım Adım Kurulum

### 1. Python Kurulumu

```bash
# Python 3.11 indirin ve kurun
# https://www.python.org/downloads/

# Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin
```

### 2. CUDA Kurulumu (GPU için)

```bash
# NVIDIA GPU sürücülerini güncelleyin
# https://www.nvidia.com/Download/index.aspx

# CUDA Toolkit 12.4 indirin
# https://developer.nvidia.com/cuda-downloads
```

### 3. Projeyi İndirin

```bash
# Git ile
git clone https://github.com/Memati8383/AI_Triggerbot.git
cd AI_Triggerbot

# VEYA ZIP olarak indirin ve çıkartın
```

### 4. Otomatik Kurulum

```bash
# INSTALL.bat dosyasını çalıştırın
# Bu işlem 5-10 dakika sürebilir
```

### 5. Model Dosyasını İndirin

```bash
# YOLO11s modelini indirin
# https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11s.pt

# models/ klasörüne koyun
AI_Triggerbot/
└── models/
    └── yolo11s.pt
```

### 6. İlk Çalıştırma

```bash
# START.bat dosyasını çalıştırın
```

## Manuel Kurulum

Otomatik kurulum çalışmazsa:

### 1. Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 2. PyTorch (GPU)

```bash
# CUDA 12.4 için
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124

# CPU için (yavaş)
pip install torch torchvision
```

### 3. Diğer Paketler

```bash
pip install ultralytics
pip install mss numpy pywin32 opencv-python
```

### 4. Test

```bash
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"
```

## Sorun Giderme

### Python Bulunamadı

```bash
# Python PATH'e ekli değil
# Kontrol Paneli → Sistem → Gelişmiş Sistem Ayarları
# Ortam Değişkenleri → Path → Python yolunu ekleyin
```

### CUDA Bulunamadı

```bash
# GPU sürücüleri güncel değil
# NVIDIA Control Panel → Help → System Information
# Driver version kontrol edin

# CUDA yeniden kurun
```

### Model Bulunamadı

```bash
# models/ klasörü yoksa oluşturun
mkdir models

# yolo11s.pt dosyasını indirin ve koyun
```

### Paket Yükleme Hatası

```bash
# pip güncelleyin
python -m pip install --upgrade pip

# Tek tek yükleyin
pip install torch
pip install ultralytics
pip install mss
pip install numpy
pip install pywin32
pip install opencv-python
```

### Virtual Environment Aktif Olmaz

```bash
# PowerShell execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Sonra tekrar deneyin
.\venv\Scripts\activate
```

## Doğrulama

Kurulum başarılı mı kontrol edin:

```bash
# Virtual environment aktif
.\venv\Scripts\activate

# Python version
python --version
# Çıktı: Python 3.11.x

# CUDA kontrol
python -c "import torch; print(torch.cuda.is_available())"
# Çıktı: True (GPU varsa)

# Paketler kontrol
python -c "import cv2, mss, ultralytics; print('OK')"
# Çıktı: OK

# Model kontrol
python -c "from ultralytics import YOLO; m = YOLO('models/yolo11s.pt'); print('Model OK')"
# Çıktı: Model OK
```

## İlk Ayarlar

### 1. Config Oluştur

```bash
# İlk çalıştırmada otomatik oluşur
python app.py
# Ctrl+C ile çıkın
```

### 2. Config Düzenle

`config.json` dosyasını açın:

```json
{
    "confidence": 0.20,
    "box_size": 400,
    "target_fps": 120,
    "window_scale": 2.0
}
```

### 3. Test Et

```bash
# START.bat ile başlatın
# F2 ile aktif edin
# Debug penceresini kontrol edin
```

## Performans Optimizasyonu

### GPU Kullanımı

```python
# config.json
{
    "use_half_precision": true  # FP16 (daha hızlı)
}
```

### FPS Artırma

```python
{
    "box_size": 300,           # Daha küçük alan
    "target_fps": 120,         # Hedef FPS
    "show_heatmap": false      # Heatmap kapat
}
```

### Bellek Optimizasyonu

```python
{
    "track_targets": false,    # Tracking kapat
    "show_trails": false       # Trails kapat
}
```

## Güncelleme

```bash
# Git ile
git pull origin main

# Paketleri güncelle
pip install --upgrade torch ultralytics

# Config'i sıfırla (gerekirse)
del config.json
```

## Kaldırma

```bash
# Virtual environment sil
rmdir /s venv

# Proje klasörünü sil
cd ..
rmdir /s AI_Triggerbot
```

## Destek

Sorun yaşıyorsanız:

1. **QUICKSTART.txt** dosyasını okuyun
2. **README.md** dosyasını okuyun
3. **GitHub Issues** açın
4. Sistem bilgilerinizi paylaşın:
   - OS version
   - Python version
   - GPU model
   - Hata mesajı

---

**🎯 Başarılı kurulum için tüm adımları takip edin!**
