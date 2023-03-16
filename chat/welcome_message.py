"""
This module print welcome message in terminal
"""

from rich_sources.console import console


def print_welcome_message(name: str) -> None:
    """ Show the welcome message username
    :param name: name of user
    :return: None
    """
    console.print("Welcome to ChatGPT-CLI", style="bold green")
    console.print(f"Hello {name}", style="bold blue")
