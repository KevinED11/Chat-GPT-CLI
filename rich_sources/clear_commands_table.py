"""
This module define clear commands table
"""
from rich.table import Table, Column

from commands.clear_commands import clear_commands

table_clear_commands: Table = Table(
    Column(header="Clear commands", justify="center"),
    header_style="bold green",
    border_style="bold green"
)
for command in clear_commands:
    table_clear_commands.add_row(command)
