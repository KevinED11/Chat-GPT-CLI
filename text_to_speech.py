from os import remove as os_remove, getcwd as os_getcwd


from gtts import gTTS
from subprocess import Popen


def text_to_speech(text: str) -> None:

    speech_from_text: gTTS = gTTS(text=text, lang="es")
    speech_from_text.save("chat-question.mp3")

    # changue commands for you reproductor
    command_play_audio: list[str] = [
        "cvlc", "--play-and-exit", "chat-question.mp3"]

    play_audio: Popen[bytes] = Popen(args=command_play_audio)

    play_audio.wait()

    play_audio.terminate()

    os_remove(f'{os_getcwd()}/chat-question.mp3')
