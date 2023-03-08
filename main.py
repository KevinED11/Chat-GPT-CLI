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
from ComandsExit import comands_exit

# chargue env variables
load_dotenv()


def main(name: str) -> str:
    """This function interact with chatgpt"""

    openai.api_key = getenv("API_KEY")

    console.print("Welcome to Chat-GPT CLI", style="bold green")
    console.print(f"Hello {name}", style="bold blue")

    while True:

        content: str = input(
            "\n¿Qué pregunta quieres hacerme? ")

        if content in comands_exit:

            confirmation: str = input(
                "\n¿De verdad quieres salir? [yes, no] ")
            if confirmation == "yes":
                console.print(
                    "\nAdiós, espero volver a verte pronto", style="bold green")
                break
            else:
                continue

        response: Response = response_chat_gpt(content=content)

        console.print(response["choices"][0]["message"]
                      ["content"], style="bold italic")


if __name__ == "__main__":
    typer.run(main)
