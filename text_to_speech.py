from gtts import gTTS
from os import remove as os_remove, getcwd as os_getcwd
from subprocess import Popen


def text_to_speech(text: str) -> None:

    speech: gTTS = gTTS(text=text, lang="es")
    speech.save("chat-question.mp3")
    # threading.Thread(target=lambda: os.system("vlc welcome.mp3 --play-and-exit")).start()
    # os.system("cvlc --play-and-exit welcome.mp3")
    command_play_audio: list[str] = [
        "cvlc", "--play-and-exit", "chat-question.mp3"]

    play_audio: Popen[bytes] = Popen(command_play_audio)

    play_audio.wait()

    play_audio.terminate()

    os_remove(f'{os_getcwd()}/chat-question.mp3')
