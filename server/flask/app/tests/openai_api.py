from app import app
from openai import OpenAI


def model(content):
    client = OpenAI(api_key="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")

    response = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-1106:personal:tutor-proj8-2:8ZJgxOYp",
    messages=[
        {"role": "system", "content": "Expert python tutor"},
        {"role": "user", "content": content}
    ],
    temperature=0,
    max_tokens=50
    )

    return(response.choices[0].message.content)