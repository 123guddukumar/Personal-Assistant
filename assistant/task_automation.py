import os
import subprocess
import psutil
import webbrowser  # For opening URLs in the web browser

# Register Firefox browser
firefox_path = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"  # Adjust path if necessary
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

def close_application(app_name):
    """Close an application by name."""
    for proc in psutil.process_iter():
        try:
            if app_name.lower() in proc.name().lower():
                proc.terminate()
                return f"Closing {app_name}."
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return f"{app_name} is not running."

def open_application(command):
    """Open an application based on the recognized command."""
    command = command.lower()
    
    if "firefox" in command:
        subprocess.Popen(firefox_path)  # Open Firefox
        return "Opening Firefox."

    elif "youtube" in command or "utub" in command:
        # Assuming Firefox is already open
        webbrowser.get('firefox').open("https://www.youtube.com")
        return "Opening YouTube in Firefox."
    
    elif "calculator" in command:
        subprocess.Popen("calc.exe")
        return "Opening Calculator."
    
    elif "notepad" in command:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad."
    
    elif "ms word" in command or "word" in command:
        subprocess.Popen(["C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"])  # Adjust path if necessary
        return "Opening Microsoft Word."
    
    return "I didn't recognize that command."

def search_youtube_video(video_title):
    """Search for a video on YouTube."""
    webbrowser.open(f"https://www.youtube.com/results?search_query={video_title}")
    return f"Searching for '{video_title}' on YouTube."

def handle_command(command):
    """Handle commands to open or close applications."""
    command = command.lower()
    
    if "close" in command:
        app_name = command.replace("close", "").strip()
        return close_application(app_name)
    
    if "open" in command:
        if "youtube" in command:
            return open_application(command)
        return open_application(command)
    
    if "play" in command and "youtube" in command:
        video_title = command.replace("play", "").replace("youtube", "").strip()
        return search_youtube_video(video_title)

    return "I didn't recognize that command."
