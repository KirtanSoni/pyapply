import json
import os
import sys

coverletter_structure = """Select the relevant skills & Experience for the job description and use them to Write 4 paragraphs tailored to the job description;
use keywords from the job description under 350 words
costraints: no Variables in Square brackets, avoid sentences that require extra information. extrapolate experience for unrelated jobs

##Structure##

I am writing to express my interest on the given jobtitle...

Educational Background related paragraph...

Previous roles related paragraph...

Relevant Skills related to job descriptions....

##Details##
"""



def load_user_data()->dict:
    base = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "user.json"
    abs_file_path = os.path.join(base, rel_path)
    try:
        with open(abs_file_path) as f:
            CONFIG = json.load(f)
    except:
        print("User Not Configured")
        #exit(1)
    return CONFIG

def load_coverletter_prompt()->str:
    base = os.path.dirname(__file__)
    abs_file_path = os.path.join(base, "coverletter.txt")
    try:
        prompt = open(abs_file_path,'r').read()
        return prompt
    except Exception as e:
        print("Prompt not Configured")
        exit(1)
        


def save_user_data(CONFIG:dict):
    base = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "user.json"
    abs_file_path = os.path.join(base, rel_path)
    with open(abs_file_path, 'w') as outfile:
        json.dump(CONFIG, outfile)
    print("User Configured")


    
def config_prompt(path)->str:
    try:
        user_prompt = open(path, 'r').read() 
    except Exception as e:
        print("Error in reading prompt file: ", e)
        return
    base = os.path.dirname(__file__)
    abs_file_path = os.path.join(base, "coverletter.txt")
    open(abs_file_path,'w').write(coverletter_structure+user_prompt)
    print("Prompt Configured")





