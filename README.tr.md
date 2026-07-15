# 🔥 Hotspot Mode - Dinamik Güncelleme Kapatıcı

*🌍 Bunu [İngilizce (English)](README.md) olarak oku.*

![Hotspot Mode Banner](banner.png)

![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![Python](https://img.shields.io/badge/Made_with-Python_3-blueviolet)
![License](https://img.shields.io/badge/License-MIT-green)

Telefonunuzun internetini paylaştığınızda (hotspot) arka planda çalışan tüm güncelleme servislerini dinamik olarak bularak durduran, akıllı ve hafif bir Windows arka plan (system tray) Python uygulaması. Windows Update, Adobe, Google ve diğer sinsi indiricilerin mobil kotanızı sömürmesini engeller.

## ✨ Özellikler

* **Dinamik Servis Avcısı:** İçinde "update" kelimesi geçen tüm servisleri PowerShell kullanarak dinamik olarak bulur. Manuel bir servis listesi tutmanıza gerek kalmaz.
* **Güvenli Geri Yükleme:** Herhangi bir servisi devre dışı bırakmadan önce, servislerin orijinal durumlarını (Otomatik, Elle, Çalışıyor, Durduruldu) tam olarak kaydeder. Hotspot bağlantınızı kestiğinizde her şey orijinal haline geri döner. Windows'u bozma riski sıfırdır.
* **Akıllı Otomatik Mod:** Tek tıkla mobil Wi-Fi ağınızı kaydedin. Uygulama, ağ bağlantılarınızı her 10 saniyede bir sessizce izler. Hotspot'unuza bağlandığınızda güncellemeleri otomatik olarak kapatır, normal bir Wi-Fi ağına geçtiğinizde ise tekrar açar.
* **Gizli Çalışma:** Sağ alt köşedeki sistem tepsisinde tamamen sessiz çalışır. 🟢 Yeşil normal durumu, 🔴 Kırmızı ise güncellemelerin engellendiğini gösterir.

## 🚀 Kurulum ve Kullanım

### Gereksinimler
Sisteminizde Python yüklü olmalıdır. Gerekli kütüphaneleri kurun:

```bash
pip install pystray pillow
```

### Scripti Çalıştırma
Bu araç temel Windows servislerine müdahale ettiği için **mutlaka Yönetici Olarak (Administrator) çalıştırılmalıdır**. Komut İstemi'ni (CMD) veya PowerShell'i yönetici olarak açıp dosyanın bulunduğu dizinde şu komutu girin:

```bash
python hotspot_mode.py
```

## 🛠️ Kullanım Talimatları

1. Scripti Yönetici olarak çalıştırın. Sağ alt köşede yeşil bir ikon belirecektir.
2. Bilgisayarınızı telefonunuzun Wi-Fi (hotspot) ağına bağlayın.
3. Yeşil ikona sağ tıklayın ve **"🎯 Şu Anki Ağı Hotspot Kaydet"** seçeneğine tıklayın.
4. İkon kırmızıya dönecek ve tüm güncelleme servislerinin askıya alındığına dair bir bildirim göreceksiniz.
5. Hotspot bağlantınızı kestiğinizde, program ağ değişikliğini algılar ve 10 saniye içinde tüm servisleri orijinal ayarlarına geri döndürür (İkon tekrar yeşil olur).

## ⚠️ Antivirüs Uyarıları (False Positive) Hakkında
Bu Python scripti Windows Update gibi servisleri programatik olarak durdurup yapılandırdığı için, bazı antivirüs yazılımları veya Windows Defender bu işlemleri şüpheli olarak işaretleyebilir. Bu durum tamamen normaldir (False Positive). Tüm kaynak kodları açık ve şeffaftır.

## 📄 Lisans
Bu proje açık kaynaktır ve MIT Lisansı ile sunulmaktadır. Özgürce çatallayabilir (fork), değiştirebilir ve geliştirebilirsiniz!
