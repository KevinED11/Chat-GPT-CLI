import openai

# context assistant
messages: list[dict[str, str]] = [
    {"role": "system", "content": ""},

]


def response_chat_gpt(user_question: str) -> dict:
    # messages[1]["content"] = content
    messages.append({"role": "user", "content": user_question})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1000,  # 300
            temperature=0.5,

        )

        text_response_assistant: str = response["choices"][0]["message"]["content"]

        total_tokens_used: int = response["usage"]["total_tokens"]

        messages.append(
            {"role": "assistant", "content": text_response_assistant})

        if total_tokens_used >= 3096:
            tokens_to_remove: int = total_tokens_used - 1000

            messages[0]["content"] = messages[0]["content"][::-tokens_to_remove]

            total_tokens_used -= tokens_to_remove

        messages[0]["content"] += "\n" + f"User input: ({user_question})" + " => response = " + \
            text_response_assistant + "\n"

        print(messages)

        print(response)

        return response

    except Exception as error:
        return error
