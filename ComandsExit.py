from enum import Enum


class ComandsExit(Enum):
    EXIT: str = "exit"
    QUIT: str = "quit"
    Q: str = "q"
    FINISH: str = "finish"
    SALIR: str = "salir"
    ADIOS: str = "adios"


comands_exit: list = [c.value for c in ComandsExit]
