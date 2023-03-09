import openai

# context assistant
messages: list[dict[str, str]] = [
    {"role": "system", "content": ""},
    {"role": "user", "content": ""}

]


def response_chat_gpt(content: str) -> list[dict]:
    messages[1]["content"] = content

    try:
        response: list[dict] = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=300,
            temperature=0.3,

        )

        messages[0]["content"] += "\n" + f"User input: ({content})" + " => response = " + \
            response["choices"][0]["message"]["content"] + "\n"

        print(messages)

        print(messages[0]["content"])

        return response

    except Exception as error:
        return error
