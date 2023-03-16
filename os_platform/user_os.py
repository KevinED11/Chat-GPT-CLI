"""
This module get operating system of user
"""
from platform import system as platform_system


def user_os() -> str:
    """ get operating system of user
    :return: str
    """
    return platform_system()
