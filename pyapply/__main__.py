# author : Kirtan Soni
import time
import pyperclip
import os
from pyapply.utils import requestgpt
from pyapply.presets.asujobs import create_folder_and_file
from pyapply.utils.parsers.coverletter import generate_cover_letter
from pyapply.config import *







jobs_summary = []
isrunning = True
if __name__ == "__main__":
    job_description = pyperclip.paste()
    print("Listening for job description...")
    while(isrunning):
        time.sleep(3)
        if job_description == pyperclip.paste():
            continue
        else:
            job_description = pyperclip.paste()

            _, jobid = create_folder_and_file(job_description)
            if _:
                print("Job ID found: ", jobid)
            else:
                print("No Job ID found")
                continue
            prompt =   prompt = open(CONFIG['prompt_path']+'/prompt.txt', 'r').read()
            _, content = requestgpt(job_description,prompt)
            if _:
                print("generated chatgpt response ")
            else:
                print("Error in generating chatgpt response")
                continue
            output_path = jobid
            generate_cover_letter(output_path,content)
            print("generated cover letter")
            try:
                os.remove(CONFIG['temp_path']+'/coverletter.pdf')
            except:
                print("Error in removing cover letter")
                continue
            try:
                os.system('cp '+output_path+'/coverletter.pdf '+CONFIG['temp_path'])
            except:
                print("Error in copying cover letter")
                continue
            jobs_summary.append(jobid)
            print("Listening for job description...")



