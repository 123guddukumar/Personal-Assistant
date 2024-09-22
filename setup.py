import speech_recognition as sr

def listen_from_specific_microphone(mic_index):
    recognizer = sr.Recognizer()

    # Use the microphone with the specified index
    with sr.Microphone(device_index=mic_index) as source:
        print(f"Listening using microphone: {sr.Microphone.list_microphone_names()[mic_index]}")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='hi-IN')
            print(f"Recognized Speech: {text}")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    # Replace '1' with the index of your Bluetooth headset from the microphone list
    listen_from_specific_microphone(mic_index=2)






# import speech_recognition as sr
# import pyttsx3

# # Set up speech recognition
# recognizer = sr.Recognizer()

# # Configure text-to-speech engine for output
# engine = pyttsx3.init()

# # Set trüke Buds S1 as output device (replace with the correct index from your list)
# engine.setProperty('voice', 'com.apple.speech.synthesis.voice.karen')  # You can configure the voice type
# engine.setProperty('rate', 150)  # Speech rate

# # List all available microphones (optional)
# def list_microphones():
#     print("Available microphones:")
#     for index, name in enumerate(sr.Microphone.list_microphone_names()):
#         print(f"Microphone with index {index}: {name}")

# def recognize_speech_from_microphone():
#     # Set the correct microphone index for input (replace with trüke Buds S1 index)
#     with sr.Microphone(device_index=2) as source:
#         print("Listening using trüke Buds S1...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#         try:
#             # Recognize speech using Google's API (convert Hindi to English)
#             recognized_text = recognizer.recognize_google(audio, language='hi-IN')
#             print(f"Recognized Speech (in Hindi): {recognized_text}")

#             # Translate recognized Hindi text to English (if needed)
#             # Here we assume you're handling translation outside the code
#             translated_text = recognized_text  # Placeholder for translation
            
#             # Output translated text (speak in Hindi)
#             engine.say(f"आपने कहा: {translated_text}")
#             engine.runAndWait()

#         except sr.UnknownValueError:
#             print("Could not understand audio.")
#         except sr.RequestError as e:
#             print(f"Error with the API request; {e}")

# if __name__ == "__main__":
#     # Optional: list all microphones for reference
#     list_microphones()
    
#     # Recognize speech and output result
#     recognize_speech_from_microphone()
