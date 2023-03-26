"""
This module plays the audio file
"""
from subprocess import Popen


from os_platform.user_os import user_os
from os_platform.options_os_platform import OptionsOsPlatform
from os_platform.supported_os import supported_os


def play_audio_file(filename: str) -> None:
    """reproduce audio file based in operating system

    :param filename: name of the mp3 file
    :return: None
    """
    operating_system: str = user_os()

    # default reproduction command for linux
    command_play_audio: list[str] = ["cvlc", "--play-and-exit", filename]

    match operating_system:
        case os_platf if os_platf in supported_os:

            if os_platf == OptionsOsPlatform.LINUX.value:
                command_play_audio: list[str] = command_play_audio

            elif os_platf == OptionsOsPlatform.WINDOWS.value:
                command_play_audio: list[str] = ["start", filename]

        case _:
            print("Unsupported operating system")

    with Popen(args=command_play_audio) as play_audio:
        play_audio.wait()

        play_audio.terminate()
