import openai


# context assistant
messages: list[dict[str, str]] = [
    {"role": "system",
     "content": "eres un asistente increible y eres el mas inteligente"
     },


]


def response_chat_gpt(user_question: str) -> dict:
    global messages
    # messages[1]["content"] = user_question
    messages.append({"role": "user", "content": user_question})

    try:
        gpt_response_question: dict = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,  # 300
            temperature=0.5,

        )
        text_response_assistant: str = gpt_response_question[
            "choices"][0]["message"]["content"]

        total_tokens_used: int = gpt_response_question["usage"]["total_tokens"]

        if total_tokens_used >= 1000:

            tokens_to_remove: int = total_tokens_used - 500

            gpt_response_question["usage"]["total_tokens"] -= tokens_to_remove

            messages = messages[:-tokens_to_remove]

            messages.insert(0, {"role": "system",
                                "content": """eres un asistente increible y
                                eres el mas inteligente"""
                                })

            messages.insert(1, {"role": "user", "content": user_question})

        messages.append(
            {"role": "assistant", "content": text_response_assistant})

        print(f"despues del if:     {messages}")

        print(gpt_response_question)

        return gpt_response_question

    except Exception as error:
        return error
