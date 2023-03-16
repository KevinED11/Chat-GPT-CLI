"""
this is principal module of the chatbot
"""
import typer


from chat.clear_terminal import clear_terminal
from chat.welcome_message import print_welcome_message
from chat.chat_loop import chat_loop
from config import load_config
from rich_sources.merged_tables import merged_tables
from rich_sources.console import console


def main(name: str, speech: bool) -> None:
    """ execute the chatbot
    :param name: str
    :param speech: bool
    :return: None
    """
    config: dict[str, any] = load_config()
    clear_terminal()

    # show welcome in terminal
    print_welcome_message(name=name)

    # commands table
    console.print("\n", merged_tables)

    # init Chat
    chat_loop(
        openai_api_key=config["openai_api_key"], name=name, speech=speech)


if __name__ == "__main__":
    typer.run(main)
