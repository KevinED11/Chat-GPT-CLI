from os import remove as os_remove, getcwd as os_getcwd


from gtts import gTTS
from audio.play_audio_file import play_audio_file


def text_to_speech(text: str) -> None:
    filename: str = "chat-question.mp3"

    text_to_voice: gTTS = gTTS(text=text, lang="es")
    text_to_voice.save("chat-question.mp3")

    if text_to_voice:
        play_audio_file(filename=filename)

    os_remove(f'{os_getcwd()}/chat-question.mp3')
