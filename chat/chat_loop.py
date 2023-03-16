"""
This module interact with openai API and
request information for conversation
"""
import openai


from chat.handle_user_question import handle_user_question
from chat.response_chat import response_chat_gpt
from console import console
from audio.text_to_speech import text_to_speech


def chat_loop(openai_api_key: str, name: str, speech: bool) -> None:
    """ Chat loop for clients to interact with GPT API
    :param openai_api_key:
    :param name:
    :param speech:
    :return: None
    """
    openai.api_key = openai_api_key

    # context assistant
    messages: list[dict[str, str]] = [
        {"role": "system",
         "content": "eres un asistente increible y eres el mas inteligente"
         },
    ]

    while True:

        # first question for interact with the chat
        user_question: str = input(
            "\n¿Qué pregunta quieres hacerme? ").lower()

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

        question_response: dict = response_chat_gpt(
            user_question=user_question, messages=messages)

        text_response: str = question_response[
            "choices"][0]["message"]["content"]

        console.print(text_response, style="bold italic")

        if speech:
            try:
                text_to_speech(text=text_response)

            except (RuntimeError,
                    FileNotFoundError, OSError,
                    KeyboardInterrupt, IOError) as error:

                if not KeyboardInterrupt:
                    speech: bool = False
                    print(
                        f"""Se desactivo la voz debido
                        a un error del sistema:  {error}""")
