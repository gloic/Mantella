from openai import OpenAI

import config


def build_messages(system_prompt, user_prompt):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def generate(messages=None, system_prompt="", prompt="",
             temperature=config.default_temp,
             top_p=config.default_top_p):
    if messages is None:
        history = build_messages(system_prompt, prompt)
    else:
        history = messages

    client = OpenAI(base_url=config.base_url, api_key=config.api_key)
    completion = client.chat.completions.create(
        model="osef",
        messages=history,
        temperature=temperature,
        top_p=top_p,
    )
    response = completion.choices[0].message.content
    return response
