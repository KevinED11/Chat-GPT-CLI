import openai
from requests import Response

# context assistant
messages: list[dict[str, str]] = [
    {"role": "system", "content": ""},

]


def response_chat_gpt(content: str) -> Response:

    messages.append({"role": "user", "content": content})

    try:
        response: Response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.3,

        )

        messages[0]["content"] += "\n" + f"User input: ({content})" + " => response = " + \
            response["choices"][0]["message"]["content"] + "\n"
        print(messages[0]["content"])

        return response

    except Exception as error:
        return error
