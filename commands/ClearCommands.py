from enum import Enum


class ClearCommands(Enum):
    CLEAR: str = "clear"
    CLS: str = "cls"
    limpiar: str = "limpiar"


clear_commands: list[str] = [c.value for c in ClearCommands]
