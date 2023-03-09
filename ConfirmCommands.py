from enum import Enum


class ConfirmCommands(Enum):
    YES: str = "yes"
    Y: str = "y"
    SI: str = "si"
    AFIRMATIVO: str = "afirmativo"


confirm_commands: list[str] = [c.value for c in ConfirmCommands]
