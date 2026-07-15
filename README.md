# 🔥 Hotspot Mode - Dynamic Update Killer

A lightweight, intelligent Windows system tray utility built with Python that dynamically hunts down and suspends all background update services when you connect to a mobile hotspot. Save your mobile data plan from aggressive Windows updates, Adobe, Google, and other hidden background downloaders.

## ✨ Features

* **Dynamic Service Hunting:** Uses PowerShell to dynamically find any service containing the word "update". You don't need to manually maintain a list of services.
* **Safe State Restoration:** Before disabling anything, it saves the exact original states of the services (Auto, Manual, Running, Stopped). When you disconnect from the hotspot, everything is restored exactly as it was. Zero risk of breaking Windows.
* **Smart Auto-Mode:** Save your mobile Wi-Fi SSID with one click. The app silently monitors your network connections every 10 seconds. It automatically disables updates when connected to your hotspot and re-enables them when you switch back to a standard Wi-Fi network.
* **Zero Console Window:** Runs completely silently in your system tray (bottom right corner). 🟢 Green means normal, 🔴 Red means updates are blocked.

## 🚀 How to Run & Build

### Prerequisites
You need Python installed on your system.

```bash
pip install pystray pillow
