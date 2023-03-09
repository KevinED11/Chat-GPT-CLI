from enum import Enum


class CommandsExit(Enum):
    EXIT: str = "exit"
    QUIT: str = "quit"
    Q: str = "q"
    FINISH: str = "finish"
    SALIR: str = "salir"
    ADIOS: str = "adios"


comands_exit: list[str] = [c.value for c in CommandsExit]
