from gtts import gTTS
from os import remove, getcwd
from subprocess import Popen


def text_to_speech(text: str) -> None:

    myobj: gTTS = gTTS(text=text, lang="es", slow=None)
    myobj.save("chat-question.mp3")
    # threading.Thread(target=lambda: os.system("vlc welcome.mp3 --play-and-exit")).start()
    # os.system("cvlc --play-and-exit welcome.mp3")
    command_play_audio: list[str] = [
        "cvlc", "--play-and-exit", "chat-question.mp3"]
    play_audio: Popen[bytes] = Popen(command_play_audio)

    play_audio.wait()

    play_audio.terminate()

    remove(f'{getcwd()}/chat-question.mp3')
