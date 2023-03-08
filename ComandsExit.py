from enum import Enum


class ComandsExit(Enum):
    EXIT: str = "exit"
    QUIT: str = "quit"
    Q: str = "q"
    SALIR: str = "salir"


comands_exit: list = [c.value for c in ComandsExit]
