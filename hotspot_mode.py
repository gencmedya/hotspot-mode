import pystray
from PIL import Image, ImageDraw
import subprocess
import threading
import time
import json
import os
import re

CONFIG_FILE = "hotspot_config.json"
STATE_FILE = "suspended_services.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"hotspot_ssid": "", "auto_mode": True}

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

config = load_config()
is_blocked = False

def run_cmd(cmd):
    subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)

def get_all_update_services():
    ps_cmd = (
        "PowerShell -ExecutionPolicy Bypass -Command "
        "\"Get-Service | Where-Object {$_.Name -like '*update*' -or $_.DisplayName -like '*update*'} "
        "| Select-Object Name, StartType, Status | ConvertTo-Json\""
    )
    result = subprocess.run(ps_cmd, shell=True, capture_output=True, text=True, encoding='utf-8', creationflags=subprocess.CREATE_NO_WINDOW)
    try:
        data = json.loads(result.stdout)
        if isinstance(data, dict):
            return [data]
        return data if isinstance(data, list) else []
    except Exception:
        return []

def map_start_type(val):
    val_str = str(val).lower()
    if "auto" in val_str or val_str == "2":
        return "auto"
    elif "manual" in val_str or "demand" in val_str or val_str == "3":
        return "demand"
    else:
        return "disabled"

def disable_updates(icon=None):
    global is_blocked
    update_services = get_all_update_services()
    saved_states = {}

    for svc in update_services:
        name = svc.get("Name")
        start_type = svc.get("StartType")
        status = svc.get("Status")
        
        if name:
            saved_states[name] = {"start_type": start_type, "status": status}
            run_cmd(f"sc config \"{name}\" start= disabled")
            run_cmd(f"net stop \"{name}\"")
            
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(saved_states, f, indent=4)

    is_blocked = True
    if icon:
        icon.icon = create_image('red')
        icon.title = "Hotspot Mode: ACTIVE (Updates Locked!)"

def enable_updates(icon=None):
    global is_blocked
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            saved_states = json.load(f)
            
        for name, state in saved_states.items():
            orig_start = map_start_type(state.get("start_type", "demand"))
            orig_status = str(state.get("status", "")).lower()
            
            run_cmd(f"sc config \"{name}\" start= {orig_start}")
            
            if "running" in orig_status or orig_status == "4":
                run_cmd(f"net start \"{name}\"")
                
        try:
            os.remove(STATE_FILE)
        except Exception:
            pass
            
    is_blocked = False
    if icon:
        icon.icon = create_image('green')
        icon.title = "Hotspot Mode: PASSIVE (System Normal)"

def get_current_ssid():
    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        match = re.search(r'^\s*SSID\s*:\s*(.*)$', result.stdout, re.MULTILINE)
        if match:
            return match.group(1).strip()
    except Exception:
        pass
    return None

def set_current_as_hotspot(icon, item):
    current_ssid = get_current_ssid()
    if current_ssid:
        config["hotspot_ssid"] = current_ssid
        save_config(config)
        icon.notify(f"'{current_ssid}' saved as Hotspot Network!", "Hotspot Mode")
    else:
        icon.notify("Not connected to any Wi-Fi network!", "Error")

def wifi_monitor_loop(icon):
    global is_blocked
    while True:
        if config["auto_mode"] and config["hotspot_ssid"]:
            current_ssid = get_current_ssid()
            
            if current_ssid == config["hotspot_ssid"]:
                if not is_blocked:
                    disable_updates(icon)
                    icon.notify("Hotspot detected. All update services suspended!", "Hotspot Mode")
            else:
                if is_blocked:
                    enable_updates(icon)
                    icon.notify("Safe network detected. Services restored.", "Hotspot Mode")
                    
        time.sleep(10)

def toggle_auto_mode(icon, item):
    config["auto_mode"] = not config["auto_mode"]
    save_config(config)
    icon.notify(f"Auto-Tracking: {'ON' if config['auto_mode'] else 'OFF'}", "Hotspot Mode")

def manual_disable(icon, item):
    disable_updates(icon)
    icon.notify("Update services disabled manually.", "Hotspot Mode")

def manual_enable(icon, item):
    enable_updates(icon)
    icon.notify("Services restored to original states.", "Hotspot Mode")

def exit_app(icon, item):
    icon.stop()

def create_image(color):
    image = Image.new('RGB', (64, 64), color=(255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle((0, 0, 64, 64), fill=color)
    return image

menu = pystray.Menu(
    pystray.MenuItem("🎯 Save Current Network as Hotspot", set_current_as_hotspot),
    pystray.MenuItem("🔄 Toggle Auto-Mode", toggle_auto_mode, checked=lambda item: config["auto_mode"]),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem("🔴 Disable Updates Manually", manual_disable),
    pystray.MenuItem("🟢 Enable Updates Manually", manual_enable),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem("Exit", exit_app)
)

icon = pystray.Icon("HotspotMode", create_image('green'), "Hotspot Mode: Standby", menu)
monitor_thread = threading.Thread(target=wifi_monitor_loop, args=(icon,), daemon=True)
monitor_thread.start()
icon.run()
