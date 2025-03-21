from openai import OpenAI

def chatgpt_get_response(promt, model="gpt-4o", role="user") -> str:
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