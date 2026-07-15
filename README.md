# 🔥 Hotspot Mode - Dynamic Update Killer

*🌍 Read this in [Turkish (Türkçe)](README.tr.md).*

A lightweight, intelligent Windows system tray utility built with Python that dynamically hunts down and suspends all background update services when you connect to a mobile hotspot. Save your mobile data plan from aggressive Windows updates, Adobe, Google, and other hidden background downloaders.

## ✨ Features

* **Dynamic Service Hunting:** Uses PowerShell to dynamically find any service containing the word "update". You don't need to manually maintain a list of services.
* **Safe State Restoration:** Before disabling anything, it saves the exact original states of the services (Auto, Manual, Running, Stopped). When you disconnect from the hotspot, everything is restored exactly as it was. Zero risk of breaking Windows.
* **Smart Auto-Mode:** Save your mobile Wi-Fi SSID with one click. The app silently monitors your network connections every 10 seconds. It automatically disables updates when connected to your hotspot and re-enables them when you switch back to a standard Wi-Fi network.
* **Zero Console Window:** Runs completely silently in your system tray (bottom right corner). 🟢 Green means normal, 🔴 Red means updates are blocked.

## 🚀 How to Run

### Prerequisites
You need Python installed on your system. Install the required libraries:

```bash
pip install pystray pillow
```

### Running the Script
Since this script interacts with core Windows services, **it must be run as an Administrator**. Open an elevated Command Prompt or PowerShell, navigate to the script's folder, and run:

```bash
python hotspot_mode.py
```

## 🛠️ Usage Instructions

1. Run the python script as Administrator. A green icon will appear in your system tray.
2. Connect your PC to your mobile phone's Wi-Fi hotspot.
3. Right-click the green tray icon and select **"🎯 Save Current Network as Hotspot"**.
4. The icon will turn red, and a notification will confirm that all update services are now suspended.
5. When you disconnect from your hotspot, the script will detect the network change and automatically restore all services within 10 seconds (Icon turns green).

## ⚠️ Note on Antivirus (False Positives)
Because this Python script programmatically stops and configures Windows Services (like Windows Update), some antivirus software or Windows Defender might flag its background processes as suspicious. This is a normal false positive. The source code is entirely open and transparent.

## 📄 License
This project is open-source and available under the MIT License. Feel free to fork, modify, and improve!
