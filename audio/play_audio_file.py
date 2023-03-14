"""
"""
from subprocess import Popen
from platform import system as platform_system
from audio.os_platform.os_platform import OsPlatform


supported_os: list[str] = [os.value for os in OsPlatform]


def play_audio_file(filename: str) -> None:
    operating_system: str = platform_system()

    match operating_system:
        case os_platf if os_platf in supported_os:

            if os_platf == OsPlatform.LINUX.value:
                command_play_audio: list[str] = [
                    "cvlc", "--play-and-exit", filename]

            elif os_platf == OsPlatform.WINDOWS.value:
                command_play_audio: list[str] = ["start", filename]

        case _:
            print("Unsupported operating system")

    with Popen(args=command_play_audio) as play_audio:
        play_audio.wait()

        play_audio.terminate()
