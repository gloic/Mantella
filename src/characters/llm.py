from openai import OpenAI

default_temp = 0.7
default_top_p = 0.7

def generate(system_prompt, prompt):
    client = OpenAI(base_url="http://ldllmedt1:5000/v1", api_key="EFLUID_DEV")
    # client = OpenAI(base_url="http://127.0.0.1:5000/v1", api_key="osef")
    completion = client.chat.completions.create(
        model="osef",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=default_temp,
        top_p=default_top_p,
    )
    response = completion.choices[0].message.content
    return response
