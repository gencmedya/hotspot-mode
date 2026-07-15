# Security Policy & Expected Behaviors

## 🛡️ Antivirus and Windows Defender Warnings (False Positives)
**IMPORTANT:** You may receive warnings from Windows Defender or your Antivirus software stating that this application is "modifying system services" or "disabling Windows Update." 

**Please ignore these warnings.** 
The entire purpose of this application is to intentionally suspend update services (like Windows Update) to save your mobile data. Because the `.exe` dynamically interacts with Windows services via PowerShell, security software flags it as a heuristic threat. This is a known, expected false positive. The source code is completely open for your review.

## Supported Versions
| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability
If you discover a legitimate security vulnerability (unrelated to the expected service manipulation), please open an Issue on this repository.
