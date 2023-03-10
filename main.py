from subprocess import Popen
from os import remove as os_remove, getcwd as os_getcwd
from gtts import gTTS
from os import getenv

import openai
import typer
from dotenv import load_dotenv
from requests import Response

from response_chat import response_chat_gpt
from console import console
from ExitCommands import exit_commands
from ConfirmCommands import confirm_commands
from text_to_speech import text_to_speech

# chargue env variables
load_dotenv()


def main(name: str, speech: bool) -> None:

    openai.api_key = getenv("API_KEY")

    console.print("Welcome to Chat-GPT CLI", style="bold green")
    console.print(f"Hello {name}", style="bold blue")

    while True:

        content: str = input("\n¿Qué pregunta quieres hacerme? ").lower()

        if content == "":
            continue

        if content in exit_commands:
            exit_confirmation: str = input(
                "\n¿De verdad quieres salir? [yes, no] ").lower()

            if exit_confirmation in confirm_commands:
                console.print(
                    f"\nAdiós {name}, espero volver a verte pronto y recuerda que eres el mejor y seras exitoso.", style="bold green")
                break
            else:
                continue

        response: list[dict] = response_chat_gpt(content=content)

        response_text: str = response["choices"][0]["message"]["content"]

        console.print(response_text, style="bold italic")

        if speech:
            text_to_speech(text=response_text)


if __name__ == "__main__":
    typer.run(main)
