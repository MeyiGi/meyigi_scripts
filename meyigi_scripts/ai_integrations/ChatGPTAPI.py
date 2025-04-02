from openai import OpenAI

def chatgpt_get_response(promt, model="gpt-4o", role="user") -> str:
    """API which allowing interact with chatgpt chat

    Args:
        promt (_type_): promt to ask chatgpt
        model (str, optional): model which we are going to use for chat. Defaults to "gpt-4o".
        role (str, optional): role for chatgpt. Defaults to "user".

    Returns:
        str: structured data output from chatgpt chat
    """
    client = OpenAI()

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": role,
                "content": promt
            }
        ]
    )

    return completion.choices[0].message.content