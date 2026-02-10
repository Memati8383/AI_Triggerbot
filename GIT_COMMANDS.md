# 🔧 Git Komutları Rehberi

## İlk Kurulum

### 1. Git Kurulumu
```bash
# Git'i indirin ve kurun
# https://git-scm.com/downloads
```

### 2. Git Yapılandırması
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Repository'yi Clone Edin
```bash
git clone https://github.com/Memati8383/AI_Triggerbot.git
cd AI_Triggerbot
```

## Temel Komutlar

### Durum Kontrolü
```bash
# Değişiklikleri göster
git status

# Değişiklikleri detaylı göster
git diff
```

### Değişiklikleri Kaydetme
```bash
# Tüm değişiklikleri ekle
git add .

# Belirli dosyayı ekle
git add app.py

# Commit yap
git commit -m "feat: yeni özellik eklendi"
```

### Push & Pull
```bash
# Değişiklikleri gönder
git push origin main

# Değişiklikleri çek
git pull origin main
```

## Branch İşlemleri

### Yeni Branch Oluşturma
```bash
# Branch oluştur ve geç
git checkout -b feature/yeni-ozellik

# Sadece oluştur
git branch feature/yeni-ozellik

# Branch'e geç
git checkout feature/yeni-ozellik
```

### Branch Listeleme
```bash
# Local branch'leri listele
git branch

# Remote branch'leri listele
git branch -r

# Tüm branch'leri listele
git branch -a
```

### Branch Silme
```bash
# Local branch sil
git branch -d feature/yeni-ozellik

# Force delete
git branch -D feature/yeni-ozellik

# Remote branch sil
git push origin --delete feature/yeni-ozellik
```

## Commit İşlemleri

### Commit Mesajları
```bash
# Conventional Commits formatı
git commit -m "feat: yeni özellik"
git commit -m "fix: bug düzeltildi"
git commit -m "docs: dokümantasyon güncellendi"
git commit -m "style: kod formatı düzenlendi"
git commit -m "refactor: kod iyileştirildi"
git commit -m "perf: performans artırıldı"
git commit -m "test: test eklendi"
git commit -m "chore: genel değişiklikler"
```

### Commit Düzenleme
```bash
# Son commit'i düzenle
git commit --amend

# Son commit mesajını değiştir
git commit --amend -m "yeni mesaj"
```

### Commit Geri Alma
```bash
# Son commit'i geri al (değişiklikleri koru)
git reset --soft HEAD~1

# Son commit'i geri al (değişiklikleri sil)
git reset --hard HEAD~1

# Belirli commit'e geri dön
git reset --hard <commit-hash>
```

## Remote İşlemleri

### Remote Ekleme
```bash
# Remote ekle
git remote add origin https://github.com/Memati8383/AI_Triggerbot.git

# Remote'ları listele
git remote -v

# Remote sil
git remote remove origin
```

### Remote Güncelleme
```bash
# Remote bilgilerini güncelle
git remote update

# Remote branch'leri temizle
git remote prune origin
```

## Merge & Rebase

### Merge
```bash
# Branch'i merge et
git checkout main
git merge feature/yeni-ozellik

# Conflict çözümü sonrası
git add .
git commit -m "merge: feature/yeni-ozellik merged"
```

### Rebase
```bash
# Branch'i rebase et
git checkout feature/yeni-ozellik
git rebase main

# Conflict çözümü sonrası
git add .
git rebase --continue

# Rebase iptal
git rebase --abort
```

## Stash İşlemleri

### Değişiklikleri Saklama
```bash
# Değişiklikleri sakla
git stash

# İsimle sakla
git stash save "work in progress"

# Stash listesi
git stash list

# Stash uygula
git stash apply

# Stash uygula ve sil
git stash pop

# Stash sil
git stash drop
```

## Log & History

### Commit Geçmişi
```bash
# Commit geçmişini göster
git log

# Kısa format
git log --oneline

# Grafik format
git log --graph --oneline --all

# Son 5 commit
git log -5

# Belirli dosyanın geçmişi
git log app.py
```

### Değişiklikleri Görme
```bash
# Son commit'teki değişiklikler
git show

# Belirli commit'teki değişiklikler
git show <commit-hash>

# İki commit arası fark
git diff <commit1> <commit2>
```

## Tag İşlemleri

### Tag Oluşturma
```bash
# Lightweight tag
git tag v1.0.0

# Annotated tag
git tag -a v1.0.0 -m "Version 1.0.0"

# Tag'leri listele
git tag

# Tag'i push et
git push origin v1.0.0

# Tüm tag'leri push et
git push origin --tags
```

### Tag Silme
```bash
# Local tag sil
git tag -d v1.0.0

# Remote tag sil
git push origin --delete v1.0.0
```

## Temizlik

### Dosya Silme
```bash
# Dosyayı git'ten sil
git rm file.txt

# Dosyayı sadece git'ten sil (disk'te kalsın)
git rm --cached file.txt

# Klasörü sil
git rm -r folder/
```

### Cache Temizleme
```bash
# Git cache'i temizle
git rm -r --cached .
git add .
git commit -m "chore: cache temizlendi"
```

## GitHub Specific

### Fork & Pull Request
```bash
# 1. Fork edin (GitHub'da)

# 2. Clone edin
git clone https://github.com/YOUR_USERNAME/AI_Triggerbot.git

# 3. Upstream ekleyin
git remote add upstream https://github.com/Memati8383/AI_Triggerbot.git

# 4. Upstream'den güncellemeleri çekin
git fetch upstream
git merge upstream/main

# 5. Branch oluşturun
git checkout -b feature/yeni-ozellik

# 6. Değişikliklerinizi yapın ve push edin
git add .
git commit -m "feat: yeni özellik"
git push origin feature/yeni-ozellik

# 7. GitHub'da Pull Request açın
```

### Issues
```bash
# Commit'te issue referansı
git commit -m "fix: bug düzeltildi #123"

# Issue'yu kapatma
git commit -m "fix: bug düzeltildi. Closes #123"
```

## Yararlı Alias'lar

```bash
# .gitconfig dosyasına ekleyin
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --graph --oneline --all'
```

Kullanım:
```bash
git st          # git status
git co main     # git checkout main
git br          # git branch
git ci -m "msg" # git commit -m "msg"
git visual      # git log --graph --oneline --all
```

## Acil Durumlar

### Yanlış Branch'te Çalıştım
```bash
# Değişiklikleri sakla
git stash

# Doğru branch'e geç
git checkout correct-branch

# Değişiklikleri uygula
git stash pop
```

### Yanlış Commit Yaptım
```bash
# Son commit'i geri al
git reset --soft HEAD~1

# Değişiklikleri düzenle
# ...

# Yeniden commit yap
git commit -m "doğru mesaj"
```

### Conflict Çözümü
```bash
# 1. Conflict'li dosyaları düzenle
# 2. Conflict marker'ları temizle (<<<<, ====, >>>>)
# 3. Dosyaları ekle
git add .

# 4. Merge/Rebase devam et
git merge --continue
# veya
git rebase --continue
```

---

**💡 İpucu:** `git help <command>` ile herhangi bir komut hakkında detaylı bilgi alabilirsiniz.
