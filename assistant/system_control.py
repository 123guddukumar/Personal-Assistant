import subprocess
import psutil
import os
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import ctypes


def set_system_volume(volume_level):
    """Set the system volume to the specified level (0-100)."""
    # Ensure the volume level is within valid range
    if not (0 <= volume_level <= 100):
        raise ValueError("Volume level must be between 0 and 100.")

    # Get the default audio device
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)

    # Set the volume (volume level is in the range 0.0 to 1.0)
    volume.SetMasterVolumeLevelScalar(volume_level / 100.0, None)

def get_volume():
    """Get the current system volume level."""
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    current_volume = volume.GetMasterVolumeLevelScalar() * 100
    return f"Current volume is {int(current_volume)}%."

def open_application(app_name):
    """Open an application by its name."""
    apps = {
        "calculator": "calc.exe",
        "notepad": "notepad.exe",
        "ms word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",  # Adjust path
        "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",  # Adjust path
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Adjust path
    }
    
    app_path = apps.get(app_name.lower())
    if app_path:
        subprocess.Popen(app_path)
        return f"Opening {app_name}."
    else:
        return f"{app_name} not found."

def close_application(app_name):
    """Close an application by its name."""
    for proc in psutil.process_iter():
        try:
            if app_name.lower() in proc.name().lower():
                proc.terminate()
                return f"Closing {app_name}."
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return f"{app_name} is not running."

def restart_system():
    """Restart the system."""
    subprocess.call(["shutdown", "/r", "/t", "1"])
    return "Restarting the system."

def shutdown_system():
    """Shut down the system."""
    subprocess.call(["shutdown", "/s", "/t", "1"])
    return "Shutting down the system."

def enable_network():
    """Enable the network adapter."""
    subprocess.call(["netsh", "interface", "set", "interface", "name=\"Wi-Fi\"", "admin=enabled"])
    return "Network enabled."

def disable_network():
    """Disable the network adapter."""
    subprocess.call(["netsh", "interface", "set", "interface", "name=\"Wi-Fi\"", "admin=disabled"])
    return "Network disabled."

def handle_system_command(command):
    """Handle various system commands."""
    command = command.lower()

    if "set volume" in command.lower():
        try:
            volume_level = int(command.split("set volume")[-1].strip().replace("%", ""))
            if 0 <= volume_level <= 100:
                set_system_volume(volume_level)
                return f"Volume set to {volume_level}%."
            else:
                return "Please provide a volume level between 0 and 100."
        except ValueError:
            return "Invalid volume level provided. Please say a valid percentage."


    
    if "open" in command:
        app_name = command.replace("open", "").strip()
        return open_application(app_name)
    
    elif "close" in command:
        app_name = command.replace("close", "").strip()
        return close_application(app_name)

    elif "restart" in command:
        return restart_system()
    
    elif "shutdown" in command:
        return shutdown_system()
    
    elif "disable network" in command:
        return disable_network()
    
    elif "enable network" in command:
        return enable_network()

    return "I didn't recognize that command."
