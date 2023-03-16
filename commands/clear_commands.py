"""
This module define the clear commands for the application
"""

from enum import Enum


class ClearCommands(Enum):
    """
    The class define options clear commands
    """
    CLEAR: str = "clear"
    CLS: str = "cls"
    LIMPIAR: str = "limpiar"


clear_commands: list[str] = [c.value for c in ClearCommands]
