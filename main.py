# import standar library on python
from os import getenv

# import thirdy parthy modules
import openai
import typer
from dotenv import load_dotenv
from requests import Response

# import my modules
from response_chat import response_chat_gpt
from console import console
from CommandsExit import comands_exit
from CommandsConfirm import comands_confirm
from text_to_speech import text_to_speech
# chargue env variables
load_dotenv()


def main(name: str) -> None:

    openai.api_key = getenv("API_KEY")

    console.print("Welcome to Chat-GPT CLI", style="bold green")
    console.print(f"Hello {name}", style="bold blue")

    while True:

        content: str = input(
            "\n¿Qué pregunta quieres hacerme? ").lower()

        if content == "":
            continue

        if content in comands_exit:
            confirmation: str = input(
                "\n¿De verdad quieres salir? [yes, no] ").lower()
            if confirmation in comands_confirm:
                console.print(
                    f"\nAdiós {name}, espero volver a verte pronto y recuerda que eres el mejor y seras exitoso.", style="bold green")
                break
            else:
                continue

        response: list[dict] = response_chat_gpt(content=content)

        response_text: str = response["choices"][0]["message"]["content"]

        console.print(response_text, style="bold italic")

        text_to_speech(text=response_text)


if __name__ == "__main__":
    typer.run(main)
