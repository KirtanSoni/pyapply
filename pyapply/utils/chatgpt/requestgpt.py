from dotenv import load_dotenv
from openai import OpenAI
from ...config import CONFIG
load_dotenv()

client = OpenAI(api_key=CONFIG["OPEN_API_KEY"])
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
