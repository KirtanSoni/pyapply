from openai import OpenAI
import time
from .userdatafiles import load_user_data, load_coverletter_prompt
from .coverletters.plainDocV1 import generate_cover_letter

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
        # if e.__getstate__()['status_code'] == 401:
        #     #raise Exception("ChatGPT: Invalid API Key. Please reset User Data")
        #     raise e #TODO: handle a case where old account api key doesnt work, print intructions to follow if that error occurs
    
    
def listener(interval: int, inputcallback, callback) -> None:
    clipboard = inputcallback()
    while True:
        if clipboard == inputcallback():
            continue
        clipboard = inputcallback()
        try:
            callback(clipboard)
            print("Listening for job descriptions...") #TODO: log using click style
        except Exception as e:
            print(e) #TODO: log using click style
            continue
        time.sleep(interval)
    

def generate_coverletter(path,job_description):
    try:
        prompt = load_coverletter_prompt() + job_description
        content = requestgpt(prompt)
        generate_cover_letter(path,content) # load user data exception
    except Exception as e:
        raise e

