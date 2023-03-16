from rich.table import Table

table_exit_commands: Table = Table(
                                   show_header=True,
                                   header_style="bold red",
                                   border_style="bold red",
                                   )
table_exit_commands.add_column("Exit commands", justify="center")
table_exit_commands.add_row("salir")
table_exit_commands.add_row("adios")
table_exit_commands.add_row("finish")
table_exit_commands.add_row("quit")
table_exit_commands.add_row("bye")
table_exit_commands.add_row("exit")
table_exit_commands.add_row("q")
