from openai import OpenAI

from .userdatafiles import load_user_data

# load user data


def requestgpt(msg):
    try:
        CONFIG = load_user_data()
        key = CONFIG["OPEN_API_KEY"]
        client = OpenAI(api_key=key)
        completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": msg}]
                )
        return completion.choices[0].message.content
    except Exception as e:
        raise e
