"""
this is principal module of chatbot
"""
import typer

from clear_terminal import clear_terminal
from welcome_message import print_welcome_message
from chat.chat_loop import chat_loop
from config import load_config


def main(name: str, speech: bool) -> None:
    """
    principal function on my application

    Args:
        user_question (str): question of user

    return:
        None
    """
    config: dict[str, any] = load_config()
    clear_terminal()

    # show welcome in terminal
    print_welcome_message(name=name)

    # init Chat
    chat_loop(
        openai_api_key=config["openai_api_key"], name=name, speech=speech)


if __name__ == "__main__":
    typer.run(main)
