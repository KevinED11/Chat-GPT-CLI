

import typer


from clear_terminal import clear_terminal
from welcome_message import print_welcome_message
from chat_loop import chat_loop
from config import load_config


def main(name: str, speech: bool) -> None:
    config: dict[str, any] = load_config()

    clear_terminal()

    # show welcome in terminal
    print_welcome_message(name=name)

    # init Chat
    chat_loop(
        openai_api_key=config["openai_api_key"], name=name, speech=speech)


if __name__ == "__main__":
    typer.run(main)
