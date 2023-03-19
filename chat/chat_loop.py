"""
This is the main module of this folder
"""
import openai
from rich.prompt import Prompt
from rich.panel import Panel
from gtts import gTTSError


from chat.handle_user_question import handle_user_question
from chat.response_chat import response_chat_gpt
from rich_sources.console import console
from audio.text_to_speech import text_to_speech


def chat_loop(openai_api_key: str, name: str, speech: bool) -> None:
    """ interact with the user
    :param openai_api_key:
    :param name:
    :param speech:
    :return: None
    """
    # API KEY
    openai.api_key = openai_api_key

    # context assistant
    messages: list[dict[str, str]] = [
        {"role": "system",
         "content": "eres un asistente increible y eres el mas inteligente"
         },
    ]

    while True:

        # first question for interact with the chat
        user_question: str = Prompt.ask("\n [cyan2 bold]Qué pregunta "
                                        "quieres hacerme [/][bold white]"
                                        ":grey_question:[/]").lower()

        # Use match for compare the content and make a desicion
        question_results_validate: tuple[str | None, bool] = \
            handle_user_question(user_question=user_question, name=name)

        question, should_exit = question_results_validate

        match should_exit:
            case True:
                break

        match question:
            case None:
                continue

        # Model gpt-3.5-turbo response based on the question
        try:
            calls: int = 1
            question_response: dict = response_chat_gpt(
                user_question=user_question, messages=messages)
        except (TimeoutError, openai.APIError,
                openai.OpenAIError, KeyError) as err:
            if not isinstance(err, TimeoutError):
                print(err)
                break

            calls += 1

            if calls == 3:
                print("Exceeded maximum number of API calls (3)")
                break
            print(err)

        #
        text_response: str = question_response[
            "choices"][0]["message"]["content"]

        # Print answer to the question
        console.print(Panel.fit(
            text_response,
            border_style="yellow1",
            title="Answer to your question",
            width=130),
            style="bold italic white"
        )

        if speech:
            try:
                text_to_speech(text=text_response)

            except (RuntimeError,
                    FileNotFoundError, OSError,
                    KeyboardInterrupt, IOError,
                    gTTSError, TimeoutError) as err:

                if not isinstance(err, KeyboardInterrupt):
                    speech: bool = False
                    print(
                        f"""Se desactivo la voz debido
                        a un error del sistema:  {err}""")
