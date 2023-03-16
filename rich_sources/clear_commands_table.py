from rich.table import Table


table_clear_commands: Table = Table(
                                    header_style="bold green",
                                    border_style="bold green"
                                    )
table_clear_commands.add_column("Clear commands", justify="center")
table_clear_commands.add_row("clear")
table_clear_commands.add_row("limpiar")
table_clear_commands.add_row("cls")
