"""
This module define options operating system
"""
from enum import Enum


class OptionsOsPlatform(Enum):
    """
    The class define options os platforms
    """
    LINUX: str = "Linux"
    WINDOWS: str = "Windows"
    MACOS: str = "Darwin"
