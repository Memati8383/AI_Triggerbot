# Contributing to AI Triggerbot

## 🤝 Katkıda Bulunma

Bu projeye katkıda bulunmak istiyorsanız, aşağıdaki adımları izleyin:

### 1. Fork & Clone
```bash
# Projeyi fork edin
# Sonra clone edin
git clone https://github.com/YOUR_USERNAME/AI_Triggerbot.git
cd AI_Triggerbot
```

### 2. Branch Oluşturun
```bash
git checkout -b feature/yeni-ozellik
```

### 3. Değişikliklerinizi Yapın
- Clean code prensiplerini takip edin
- Modüler yapıyı koruyun
- Yorum satırları ekleyin
- Dokümantasyonu güncelleyin

### 4. Test Edin
```bash
# Virtual environment oluşturun
python -m venv venv
.\venv\Scripts\activate

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Uygulamayı test edin
python app.py
```

### 5. Commit & Push
```bash
git add .
git commit -m "feat: yeni özellik eklendi"
git push origin feature/yeni-ozellik
```

### 6. Pull Request Oluşturun
- GitHub'da pull request açın
- Değişikliklerinizi açıklayın
- Ekran görüntüleri ekleyin (varsa)

## 📝 Commit Mesajları

Conventional Commits formatını kullanın:

- `feat:` - Yeni özellik
- `fix:` - Bug düzeltme
- `docs:` - Dokümantasyon
- `style:` - Kod formatı
- `refactor:` - Kod iyileştirme
- `perf:` - Performans iyileştirme
- `test:` - Test ekleme
- `chore:` - Diğer değişiklikler

Örnekler:
```
feat: heatmap tracking özelliği eklendi
fix: debug penceresi RGB/BGR hatası düzeltildi
docs: README.md güncellendi
perf: FPS 120'ye çıkarıldı
```

## 🏗️ Kod Standartları

### Python Style Guide
- PEP 8 standartlarını takip edin
- Type hints kullanın
- Docstring'ler ekleyin
- Fonksiyon ve değişken isimleri açıklayıcı olsun

### Modüler Yapı
```
core/       - Çekirdek işlevsellik
ui/         - Kullanıcı arayüzü
utils/      - Yardımcı fonksiyonlar
```

### Örnek Kod
```python
def calculate_distance(x1: float, y1: float, 
                      x2: float, y2: float) -> float:
    """
    Calculate Euclidean distance between two points
    
    Args:
        x1, y1: First point coordinates
        x2, y2: Second point coordinates
        
    Returns:
        Distance as float
    """
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
```

## 🐛 Bug Raporlama

Issue açarken şunları ekleyin:
- Açık başlık
- Detaylı açıklama
- Adım adım tekrar etme yöntemi
- Beklenen davranış
- Gerçek davranış
- Ekran görüntüleri
- Sistem bilgileri (OS, Python version, GPU)

## 💡 Özellik Önerileri

Yeni özellik önerirken:
- Özelliğin amacını açıklayın
- Kullanım senaryoları verin
- Mockup/sketch ekleyin (varsa)
- Teknik detaylar verin

## ⚠️ Önemli Notlar

- Bu proje **sadece eğitim amaçlıdır**
- Online oyunlarda kullanım için değildir
- Anti-cheat sistemlerini atlatma amaçlı değildir
- Etik kullanım sorumluluğu kullanıcıya aittir

## 📧 İletişim

- Issues: GitHub Issues kullanın
- Discussions: GitHub Discussions kullanın
- Email: Proje sahibine ulaşın

## 🙏 Teşekkürler

Katkılarınız için teşekkür ederiz! 🎯
