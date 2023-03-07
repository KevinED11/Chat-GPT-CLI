# import standar library on python
import os
# import thirdy parthy modules
import typer
from rich import print, pretty, table
import openai
from dotenv import load_dotenv
from requests import Response

# chargue env variables
load_dotenv()


def main(name: str) -> str:

    openai.api_key = os.getenv("API_KEY")

    print(f"[bold italic blue]hello {name}[/bold italic blue]")

    while True:

        content: str = input("\n¿Que pregunta quieres hacerme? ")

        if content == "exit":
            return

        response: Response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": content},
            ],
            max_tokens=120,

        )

        print(response["choices"][0]["message"]["content"])


if __name__ == "__main__":
    typer.run(main)
