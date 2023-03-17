"""
This module define environment variables
and program configuration
"""
from os import getenv as os_getenv
from dotenv import load_dotenv


def load_config() -> dict[str, any]:
    """ Load config in main function of chatbot
    :return: dict[str, any]
    """

    load_dotenv()

    config: dict[str, any] = {
        "openai_api_key": os_getenv("OPENAI_API_KEY")

    }

    return config
