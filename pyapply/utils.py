from openai import OpenAI
import time
from .userdatafiles import load_user_data, load_coverletter_prompt
from .coverletters.plainV1 import generate_cover_letter

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
    
def listener(interval: int, inputcallback, callback) -> None:
    clipboard = inputcallback()
    while True:
        if clipboard == inputcallback():
            continue
        clipboard = inputcallback()
        try:
            callback(clipboard)
        except Exception as e:
            yield e
            continue
        time.sleep(interval)

def generate_coverletter(path,job_description):
    try:
        prompt = load_coverletter_prompt() + job_description
        content = requestgpt(prompt)
        generate_cover_letter(path,content)
    except Exception as e:
        raise e
    
