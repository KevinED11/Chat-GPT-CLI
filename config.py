from dotenv import load_dotenv
from os import getenv as os_getenv


def load_config() -> dict[str, any]:
    load_dotenv()

    config: dict[str, any] = {
        "openai_api_key": os_getenv("OPENAI_API_KEY")

    }

    return config
