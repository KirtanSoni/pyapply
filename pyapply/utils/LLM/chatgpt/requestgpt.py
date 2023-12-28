from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI()
def requestgpt(msg, prompt):
    mes = prompt + msg
    try:
        completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": mes}]
                )
        return True,completion.choices[0].message.content
    except Exception as e:
        return False,e
