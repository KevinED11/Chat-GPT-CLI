"""
This module merged tables of exit commands and clear commands
"""

from rich.table import Table, Column
from rich.box import DOUBLE


from rich_sources.exit_commands_table import table_exit_commands
from rich_sources.clear_commands_table import table_clear_commands


merged_tables: Table = Table(
    Column(header="Exit commands"),
    Column(header="Clear commands"),
    title="Commands", show_header=False, title_style="bold",
    highlight=True, box=DOUBLE
)

merged_tables.add_row(table_exit_commands, table_clear_commands)
