"""
This module handle user question for make a decision based in the content
"""
from rich.prompt import Prompt

from commands.clear_commands import clear_commands
from commands.exit_commands import exit_commands
from commands.confirm_commands import confirm_commands
from chat.clear_terminal import clear_terminal
from chat.welcome_message import print_welcome_message
from rich_sources.console import console
from rich_sources.merged_tables import merged_tables


def handle_user_question(user_question: str,
                         name: str) -> tuple[str | None, bool]:
    """ handle user question
    :param user_question:
    :param name:
    :return: tuple[str | None, bool]
    """

    chat_continue: tuple[None, bool] = (None, False)

    chat_exit: tuple[None, bool] = (None, True)

    question_input: tuple[str, bool] = (user_question, False)

    match user_question:
        case (exit_comm) if exit_comm in exit_commands:
            exit_confirmation: str = Prompt.ask(
                "\n[yellow1 bold] ¿De verdad quieres salir?[/] "
                "([green1 bold]yes[/], [red bold]no[/])").lower()

            if exit_confirmation in confirm_commands:
                console.print(f"""\n Adiós {name}, espero volver a verte pronto
 y recuerda que eres el mejor y seras exitoso.""",
                              style="bold green")

                return chat_exit

            return chat_continue

        case (clear_comm) if clear_comm in clear_commands:
            clear_terminal()

            # Welcome message
            print_welcome_message(name=name)

            # commands table
            console.print("\n", merged_tables)

            return chat_continue

        case "":
            return chat_continue

        case _:
            return question_input
