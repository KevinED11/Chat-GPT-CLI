from console import console


def print_welcome_message(name: str) -> None:

    console.print("Welcome to ChatGPT-CLI", style="bold green")
    console.print(f"Hello {name}", style="bold blue")
