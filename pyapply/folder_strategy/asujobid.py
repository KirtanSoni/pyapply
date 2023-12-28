import os
from pyapply.config import CONFIG
import re

def create_folder_and_file(description_text):
    match = re.search(r'\b(\d+BR)\b', description_text)
    if match:
        folder_id = match.group(1)
        folder_path = CONFIG["history_path"] +"/"+ folder_id
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, 'description.txt')
        with open(file_path, 'w') as file:
            file.write(description_text)
        return True, folder_path
    else:
        return False,"No Job ID found"

