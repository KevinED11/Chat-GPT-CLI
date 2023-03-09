from enum import Enum


class CommandsConfirm(Enum):
    YES: str = "yes"
    Y: str = "y"
    SI: str = "si"
    AFIRMATIVO: str = "afirmativo"


comands_confirm: list[str] = [c.value for c in CommandsConfirm]

