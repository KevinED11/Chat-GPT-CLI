import openai


from handle_user_question import handle_user_question
from response_chat import response_chat_gpt
from console import console
from text_to_speech import text_to_speech


def chat_loop(openai_api_key: str, name: str, speech: bool) -> None:
    openai.api_key = openai_api_key

    while True:

        # first question for interact with the chat
        user_question: str = input(
            "\n¿Qué pregunta quieres hacerme? ").lower()

        # Use match for compare the content on the user quesion variable and make a desicion
        question_results_validate: tuple[str | None, bool] = handle_user_question(
            user_question=user_question, name=name)

        # unpacking tupple for to make a desicion, question return None o text and should exit True or False
        question, should_exit = question_results_validate

        match should_exit:
            case True:
                break

        match question:
            case None:
                continue

        # Model gpt-3.5-turbo response based on the question

        question_response = response_chat_gpt(user_question=user_question)

        text_response: str = question_response["choices"][0]["message"]["content"]

        console.print(text_response, style="bold italic")

        if speech:
            try:
                text_to_speech(text=text_response)
            except (ValueError, RuntimeError, FileNotFoundError, OSError) as error:
                print(f"the error is {error}")
                continue
