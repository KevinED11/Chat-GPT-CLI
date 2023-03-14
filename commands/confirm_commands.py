"""
This module define the confirm commands for the aplicattion
"""


from enum import Enum


class ConfirmCommands(Enum):
    """
    Class for define confirm exit commands
    """
    YES: str = "yes"
    Y: str = "y"
    SI: str = "si"
    AFIRMATIVO: str = "afirmativo"


confirm_commands: list[str] = [c.value for c in ConfirmCommands]
