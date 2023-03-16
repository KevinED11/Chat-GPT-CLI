import speech_recognition as sr


def voice_recognition() -> str:
    recognition: sr.Recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo")
        audio = recognition.listen(source)

    text: str = recognition.recognize_google(audio_data=audio, language="es-MX")
    print(f"Las palabras que mencionaste son: {text}")

    return text
