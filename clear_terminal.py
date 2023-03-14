"""
This module clear user terminal
"""
from os import system as os_system


def clear_terminal() -> None:
    """
    clear user terminal

    Arguments:
    no arguments

    return:
        None

    """
    os_system(command="clear")
