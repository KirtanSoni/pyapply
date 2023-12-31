import os
import re
from ..userdatafiles import load_user_data, load_coverletter_prompt
from .._requestgpt import requestgpt

# change import for different cover letter templates
from ..coverletters.plainV1 import generate_cover_letter




def create_folder_and_file(description_text):
    try:
        CONFIG = load_user_data()
        base_dir = os.path.join(CONFIG['path'],'asujobs')
        os.makedirs(base_dir, exist_ok=True)
        history_dir = os.path.join(base_dir , 'history')
        os.makedirs(history_dir, exist_ok=True)
    except Exception as e:
        raise e
    match = re.search(r'\b(\d+BR)\b', description_text)
    if match:
        job_id = match.group(1)
        job_path = os.path.join(history_dir , job_id)
        os.makedirs(job_path, exist_ok=True)

        file_path = os.path.join(job_path,'description.txt')
        with open(file_path, 'w') as file:
            file.write(description_text)
        return True, job_path
    else:
        return False,"No Job ID found"


def asujobs(job_description):
    try:
        CONFIG = load_user_data()
        base_dir = os.path.join(CONFIG['path'],'asujobs')
        os.makedirs(base_dir, exist_ok=True)
        history_dir = os.path.join(base_dir , 'history')
        os.makedirs(history_dir, exist_ok=True)
    except Exception as e:
        raise e
    _, job_path = create_folder_and_file(job_description)
    if _:
        print("Job ID found: ", job_path)
    else:
        print("No Job ID found")
        return
    print("requesting GPT 3.5...")

    prompt = load_coverletter_prompt() + job_description
    try:
        content = requestgpt(prompt)
        print("Response recieved")
        generate_cover_letter(job_path,content)
        print("generated cover letter")
    except Exception as e:
        raise e
    
    try:
        temp_coverletter = os.path.join(CONFIG['path'],'coverletter.pdf')
        os.remove(temp_coverletter)
    except:
        pass
    try:
        os.system('cp '+job_path+'/coverletter.pdf '+base_dir)
    except:
        pass
    print("Listening for job description...")