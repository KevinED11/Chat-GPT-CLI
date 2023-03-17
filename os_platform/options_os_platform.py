"""
This module define options operating system
and this is the main module of this folder
"""
from enum import Enum


class OptionsOsPlatform(Enum):
    """
    The class define operating system options
    """
    LINUX: str = "Linux"
    WINDOWS: str = "Windows"
    MACOS: str = "Darwin"
