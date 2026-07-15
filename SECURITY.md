# Security Policy & Expected Behaviors

## 🛡️ Antivirus and Windows Defender Warnings (False Positives)
**IMPORTANT:** You may receive warnings from Windows Defender or your Antivirus software stating that this script is "modifying system services" or "disabling Windows Update." 

**Please ignore these warnings.** The entire purpose of this Python script is to intentionally suspend update services (like Windows Update) to save your mobile data. Because the script dynamically interacts with Windows services via PowerShell, security software flags it as a heuristic threat. This is a known, expected false positive. The source code is completely open for your review.

## Supported Versions
| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability
If you discover a legitimate security vulnerability (unrelated to the expected service manipulation), please open an Issue on this repository.

---

# Güvenlik Politikası ve Beklenen Durumlar

## 🛡️ Antivirüs ve Windows Defender Uyarıları (False Positive)
**ÖNEMLİ:** Windows Defender veya Antivirüs yazılımınızdan bu scriptin "sistem hizmetlerini değiştirdiği" veya "Windows Update'i kapattığı" yönünde uyarılar alabilirsiniz.

**Lütfen bu uyarıları görmezden gelin.**
Bu uygulamanın yegane amacı, mobil kotanızı korumak için güncelleme servislerini (Windows Update vb.) bilinçli olarak durdurmaktır. Python kodu, PowerShell üzerinden dinamik olarak işlem yaptığı için güvenlik yazılımları bunu şüpheli (heuristic) bir hareket olarak algılar. Bu tamamen beklenen bir durumdur (False Positive). İçinizin rahat etmesi için tüm kaynak kodlarımız şeffaf bir şekilde incelemenize açıktır.

## Desteklenen Sürümler
| Sürüm   | Destek Durumu      |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Güvenlik Açığı Bildirme
Eğer (beklenen servis müdahaleleri dışında) yazılımda gerçek bir güvenlik açığı keşfederseniz, lütfen bu depo (repository) üzerinden bir "Issue" oluşturarak bize bildirin.
