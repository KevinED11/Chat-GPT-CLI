"""
This module define environment variables
and configuration on program
"""
from os import getenv as os_getenv


from dotenv import load_dotenv


def load_config() -> dict[str, any]:
    """
    Load configuration in the principal function
    named main using environment variales
    """
    load_dotenv()

    config: dict[str, any] = {
        "openai_api_key": os_getenv("OPENAI_API_KEY")

    }

    return config
