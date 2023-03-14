"""
This module handle user question for make a desicion based in the content
"""
from commands.clear_commands import clear_commands
from commands.exit_commands import exit_commands
from commands.confirm_commands import confirm_commands
from clear_terminal import clear_terminal
from welcome_message import print_welcome_message
from console import console


def handle_user_question(user_question: str,
                         name: str) -> tuple[str | None, bool]:
    """
    """

    chat_continue: tuple[None, bool] = (None, False)

    chat_exit: tuple[None, bool] = (None, True)

    question_input: tuple[str, bool] = (user_question, False)

    match user_question:
        case (exit_comm) if exit_comm in exit_commands:
            exit_confirmation: str = input(
                "\n¿De verdad quieres salir? [yes, no] ").lower()

            if exit_confirmation in confirm_commands:
                console.print(f"""\nAdiós {name}, espero volver a verte pronto
y recuerda que eres el mejor y seras exitoso.""",
                              style="bold green")

                return chat_exit

            return chat_continue

        case (clear_comm) if clear_comm in clear_commands:
            clear_terminal()

            print_welcome_message(name=name)

            return chat_continue

        case "":
            return chat_continue

        case _:
            return question_input
