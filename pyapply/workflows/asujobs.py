import os
from pyapply.utils import requestgpt, generate_cover_letter
from pyapply.folder_strategy import create_folder_and_file
from pyapply.config import CONFIG

def asujobs(job_description):
    _, jobid = create_folder_and_file(job_description)
    if _:
        print("Job ID found: ", jobid)
    else:
        print("No Job ID found")
        return
    print("requesting GPT 3.5...")
    prompt = open(CONFIG['prompt_path']+'/coverletter.txt', 'r').read()
    _, content = requestgpt(job_description,prompt)
    if _:
        print("generated chatgpt response ")
    else:
        print("Error in generating chatgpt response")
        return
    output_path = jobid
    generate_cover_letter(output_path,content)
    print("generated cover letter")
    try:
        os.remove(CONFIG['path']+'/coverletter.pdf')
    except:
        print("Error in removing cover letter")
        return
    try:
        os.system('cp '+output_path+'/coverletter.pdf '+CONFIG['path'])
    except:
        print("Error in copying cover letter")
        return
    print("Listening for job description...")