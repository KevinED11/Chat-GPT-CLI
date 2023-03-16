"""
This module clear user terminal
"""
from os import system as os_system


from os_platform.user_os import user_os
from os_platform.options_os_platform import OptionsOsPlatform
from os_platform.supported_os import supported_os


def clear_terminal() -> None:
    """clear user terminal
    :return: None
    """
    operating_system: str = user_os()

    match operating_system:
        case os_platf if os_platf in supported_os:

            if os_platf in (OptionsOsPlatform.LINUX.value,
                            OptionsOsPlatform.MACOS.value):
                os_system(command="clear")
            elif os_platf == OptionsOsPlatform.WINDOWS.value:
                os_system(command="cls")
