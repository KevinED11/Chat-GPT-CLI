import openai


# context assistant
messages: list[dict[str, str]] = [
    {"role": "system", "content": "eres un asistente increible y eres el mas inteligente"},

]


def response_chat_gpt(user_question: str) -> dict:
    messages.append({"role": "user", "content": user_question})

    try:
        gpt_response_question = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1000,  # 300
            temperature=0.5,

        )

        text_response_assistant: str = gpt_response_question["choices"][0]["message"]["content"]

        messages.append(
            {"role": "assistant", "content": text_response_assistant})

        print(messages)

        print(gpt_response_question)

        return gpt_response_question

    except Exception as error:
        return error
