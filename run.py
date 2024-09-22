# from ui.main_window import MainWindow
from assistant.voice_command import main as voice_main

def main():
    # Initialize the main application window
    # app = MainWindow()
    
    # Start the voice recognition loop or background service if needed
    voice_main()  # This can call the main function from voice_command.py

if __name__ == "__main__":
    main()
