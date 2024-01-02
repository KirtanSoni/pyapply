import os
import re
from ..userdatafiles import load_user_data
from ..utils import generate_coverletter


# change import for different cover letter templates


def create_folder_and_file(description_text):
    try:
        CONFIG = load_user_data()
        base_dir = os.path.join(CONFIG['path'],'asujobs')
        history_dir = os.path.join(base_dir , 'history')
        os.makedirs(base_dir, exist_ok=True)
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
    try:_, job_path = create_folder_and_file(job_description)
    except Exception as e:
        print("Error in creating folder and file: ", e)
        return
    if not _:
        print(job_path)
        return
    try: generate_coverletter(job_path,job_description)
    except Exception as e:
        print("Error in generating cover letter: ", e)
        return