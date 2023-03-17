"""
This module define exit commands table
"""
from rich.table import Table, Column

from commands.exit_commands import exit_commands

table_exit_commands: Table = Table(
    Column(header="Exit commands", justify="center"),
    show_header=True,
    header_style="bold red",
    border_style="bold red",
)
for command in exit_commands:
    table_exit_commands.add_row(command)
