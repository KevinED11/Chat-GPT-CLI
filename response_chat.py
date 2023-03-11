import openai

# context assistant
messages: list[dict[str, str]] = [
    {"role": "system", "content": ""},
    {"role": "user", "content": ""}

]


def response_chat_gpt(content: str) -> dict:
    messages[1]["content"] = content

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1000,  # 300
            temperature=0.5,

        )

        total_tokens_used: int = response["usage"]["total_tokens"]
        if total_tokens_used >= 400:
            tokens_to_remove: int = 200
            messages[0]["content"] = messages[0]["content"][:-tokens_to_remove]

            response["usage"]["total_tokens"] -= tokens_to_remove

        messages[0]["content"] += "\n" + f"User input: ({content})" + " => response = " + \
            response["choices"][0]["message"]["content"] + "\n"

        print(messages)

        print(response)

        return response

    except Exception as error:
        return error
