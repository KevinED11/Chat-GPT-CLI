"""
This module creates a console object using the rich library
"""

import os
from rich.console import Console

console: Console = Console(color_system="auto")


# print(os.environ["PWD"])
# print(os.environ.get("PWD"))
