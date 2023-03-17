"""
This module print welcome message in terminal
"""


from rich_sources.console import console


def print_welcome_message(name: str) -> None:
    """ Show the welcome message username
    :param name: name of user
    :return: None
    """
    console.print(
        "\n  Welcome to ChatGPT-CLI [white]:globe_showing_americas:[/]",
        style="bold green")
    console.print(
        f"  Hello [yellow]{name}[/] [red]:red_heart-emoji:[/]",
        style="bold magenta2")
