from rich.table import Table


from rich_sources.exit_commands_table import table_exit_commands
from rich_sources.clear_commands_table import table_clear_commands


merged_tables: Table = Table(title="Commands")
merged_tables.add_column("Exit_commands", justify="center")
merged_tables.add_column("Clear commands", justify="center")
merged_tables.add_row(table_exit_commands, table_clear_commands)
