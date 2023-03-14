"""
This module define the exit commands for the aplicattion
"""
from enum import Enum


class ExitCommands(Enum):
    """
    Class for define options exit commands
    """
    EXIT: str = "exit"
    QUIT: str = "quit"
    Q: str = "q"
    FINISH: str = "finish"
    SALIR: str = "salir"
    ADIOS: str = "adios"
    BYE: str = "bye"


exit_commands: list[str] = [c.value for c in ExitCommands]
