from os import getenv as os_getenv


import typer
from dotenv import load_dotenv


from welcome_message import print_welcome_message
from chat_loop import chat_loop


# chargue env variables
load_dotenv()


def main(name: str, speech: bool) -> None:
    openai_api_key: str = os_getenv("OPENAI_API_KEY")

    # show welcome in terminal
    print_welcome_message(name=name)

    # init Chat
    chat_loop(openai_api_key=openai_api_key, name=name, speech=speech)


if __name__ == "__main__":
    typer.run(main)
