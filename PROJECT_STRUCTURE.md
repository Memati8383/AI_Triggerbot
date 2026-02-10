# 📁 Proje Yapısı

## Temiz ve Organize Dosya Sistemi

```
AI_Triggerbot/
│
├── 🚀 BAŞLATMA DOSYALARI
│   ├── START.bat              # Ana başlatma scripti
│   ├── INSTALL.bat            # İlk kurulum scripti
│   └── QUICKSTART.txt         # Hızlı başlangıç rehberi
│
├── 📖 DOKÜMANTASYON
│   ├── README.md              # Ana dokümantasyon
│   └── PROJECT_STRUCTURE.md  # Bu dosya
│
├── ⚙️ KONFİGÜRASYON
│   ├── config.json            # Ayarlar (otomatik oluşur)
│   └── requirements.txt       # Python bağımlılıkları
│
├── 🎯 ANA UYGULAMA
│   └── app.py                 # Ana program (Clean Architecture)
│
├── 🔧 CORE MODÜLLER (Çekirdek)
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Konfigürasyon yönetimi
│   │   ├── detector.py        # AI tespit motoru (YOLO)
│   │   ├── screen_capture.py # Ekran yakalama
│   │   ├── aim_controller.py # Nişan ve ateş kontrolü
│   │   └── target_manager.py # Hedef yönetimi
│
├── 🖼️ UI MODÜLLER (Arayüz)
│   └── ui/
│       ├── __init__.py
│       └── visualizer.py      # Debug penceresi (2x büyük)
│
├── 🛠️ UTILS MODÜLLER (Yardımcı)
│   └── utils/
│       ├── __init__.py
│       ├── performance.py     # FPS ve performans izleme
│       └── input_handler.py   # Klavye girişi yönetimi
│
├── 🌟 GELİŞMİŞ ÖZELLİKLER
│   └── advanced_features.py   # Heatmap, Tracker, Sound, vb.
│
├── 🤖 AI MODEL
│   └── models/
│       └── yolo11s.pt         # YOLO11 model dosyası
│
└── 📦 VIRTUAL ENVIRONMENT
    └── venv/                  # Python sanal ortamı
```

## Modül Açıklamaları

### 🔧 Core Modüller
**Sorumluluk**: Uygulamanın temel işlevselliği

- **config.py**: Tüm ayarları yönetir (load/save/get/set)
- **detector.py**: YOLO model ile AI tespiti yapar
- **screen_capture.py**: Ekran görüntüsü yakalar
- **aim_controller.py**: Mouse hareketi ve ateş kontrolü
- **target_manager.py**: Hedef seçimi ve önceliklendirme

### 🖼️ UI Modüller
**Sorumluluk**: Görsel arayüz ve feedback

- **visualizer.py**: Debug penceresi, istatistikler, görselleştirme

### 🛠️ Utils Modüller
**Sorumluluk**: Yardımcı fonksiyonlar

- **performance.py**: FPS hesaplama, timing, optimizasyon
- **input_handler.py**: Klavye girişi, hotkey yönetimi

### 🌟 Advanced Features
**Sorumluluk**: Gelişmiş özellikler

- Heatmap tracking
- Target ID system
- Sound alerts
- Profile manager
- Anti-detection

## Veri Akışı

```
┌─────────────┐
│   START.bat │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   app.py    │ ◄─── Ana Uygulama
└──────┬──────┘
       │
       ├──► core/screen_capture.py  → Ekran yakala
       │         │
       │         ▼
       ├──► core/detector.py        → AI tespit
       │         │
       │         ▼
       ├──► core/target_manager.py  → Hedef seç
       │         │
       │         ▼
       ├──► core/aim_controller.py  → Nişan al & Ateş et
       │
       ├──► ui/visualizer.py        → Debug göster
       │
       └──► utils/performance.py    → FPS izle
```

## Dosya Boyutları (Yaklaşık)

```
app.py                  ~15 KB   (Ana uygulama)
core/detector.py        ~4 KB    (AI tespit)
core/aim_controller.py  ~5 KB    (Nişan kontrolü)
ui/visualizer.py        ~8 KB    (Debug penceresi)
advanced_features.py    ~10 KB   (Gelişmiş özellikler)
models/yolo11s.pt       ~22 MB   (AI model)
```

## Kullanım Senaryoları

### Senaryo 1: İlk Kurulum
```
1. INSTALL.bat çalıştır
2. Bağımlılıklar yüklensin
3. Model dosyasını koy
4. START.bat ile başlat
```

### Senaryo 2: Normal Kullanım
```
1. START.bat çalıştır
2. F2 ile aktif et
3. Oyunu aç
4. Kullan
```

### Senaryo 3: Ayar Değiştirme
```
1. Oyun içinde F3/F4 ile confidence ayarla
2. F10 ile profil değiştir
3. F6 ile kaydet
```

### Senaryo 4: Sorun Giderme
```
1. config.json'u sil
2. START.bat ile yeniden başlat
3. Varsayılan ayarlar yüklenir
```

## Temizlik ve Bakım

### Gereksiz Dosyalar Silindi ✅
- ❌ main.py (eski)
- ❌ main_ultimate.py (eski)
- ❌ quick_fix.py (test)
- ❌ test_simple.py (test)
- ❌ run.bat (eski)
- ❌ start_ultimate.bat (eski)
- ❌ README_ULTIMATE.md (eski)
- ❌ FEATURES_COMPARISON.md (gereksiz)

### Kalan Dosyalar ✅
- ✅ START.bat (tek başlatma scripti)
- ✅ INSTALL.bat (kurulum)
- ✅ app.py (ana uygulama)
- ✅ README.md (dokümantasyon)
- ✅ QUICKSTART.txt (hızlı rehber)
- ✅ Modüler yapı (core/ui/utils)

## Avantajlar

### 🎯 Organizasyon
- Her şey yerli yerinde
- Kolay bulunur
- Anlaşılır yapı

### 🚀 Performans
- Gereksiz dosya yok
- Hızlı yükleme
- Optimize edilmiş

### 🔧 Bakım
- Kolay güncelleme
- Modüler yapı
- Test edilebilir

### 📖 Dokümantasyon
- Açık ve net
- Hızlı başlangıç
- Detaylı rehber

---

**🎯 Temiz, Organize, Profesyonel!**
