import speech_recognition as sr
import pyttsx3
from googletrans import Translator
from assistant.task_automation import handle_command
from assistant.system_control import handle_system_command

from assistant.chatgpt_api import ask_chatgpt, save_conversation

def initialize_tts():
    """Initialize the text-to-speech engine."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
    return engine

def speak(text, engine):
    """Speak the provided text."""
    engine.say(text)
    engine.runAndWait()

def recognize_hindi_speech():
    """Recognize Hindi speech and convert to English."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone(device_index=2) as source:
        print("Listening for Hindi speech...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for audio

    try:
        # Recognize the speech using Google Web Speech API
        hindi_text = recognizer.recognize_google(audio, language='hi-IN')
        print(f"Recognized Hindi: {hindi_text}")
        return hindi_text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def translate_hindi_to_english(hindi_text):
    """Translate Hindi text to English."""
    translator = Translator()
    translated = translator.translate(hindi_text, src='hi', dest='en')
    return translated.text

def handle_system_command(command):
    """Handle system-level commands based on user input."""
    if "ask" in command.lower():  # Check if the command is a question
        question = command.lower().replace("ask", "").strip()
        answer = ask_chatgpt(question)
        save_conversation(question, answer)  # Save the question and answer
        return answer

def main():
    """Main function to run the speech recognition and command handling."""
    # Initialize TTS
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust as needed
    engine.setProperty('volume', 1.0)  # Adjust as needed

    while True:
        hindi_text = recognize_hindi_speech()
        
        if hindi_text:
            english_text = translate_hindi_to_english(hindi_text)
            print(f"Translated English: {english_text}")

            # Handle system commands
            response = handle_system_command(english_text)
            print(response)

            # Speak the response
            speak(response, engine)

            if "closing the assistant" in response.lower():
                break
