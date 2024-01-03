import json
import os

user_file_name = "user.json"
user_prompt_file_name = "coverletter.txt"

## Config Structure ##
class Config:
    def __init__(self, api:str, path:str, name:str, address:str, email:str):
        self.api_key = api
        self.name = name
        self.address = address
        self.email = email
        self.path = path

    def dump(self,path:str):
        with open(path, 'w') as json_file:
            json.dump( {
                'OPEN_API_KEY': self.api_key,
                'name' : self.name,
                'address' : self.address,
                'email' : self.email,
                'path' : self.path,
            },json_file)
    



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
    abs_file_path = os.path.join(base, user_file_name)
    try:
        with open(abs_file_path) as f:
            return json.load(f)
    except:
        raise Exception("User not Configured")


def load_coverletter_prompt()->str:
    base = os.path.dirname(__file__)
    abs_file_path = os.path.join(base, user_prompt_file_name)
    try:
        prompt = open(abs_file_path,'r').read()
        return prompt
    except Exception as e:
        raise Exception("Prompt not Configured")


def save_user_data(CONFIG:Config):
    base = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = os.path.join(base, user_file_name)
    CONFIG.dump(abs_file_path)


def config_prompt(path):
    try:
        user_prompt = open(path, 'r').read() 
    except Exception as e:
       raise e
    base = os.path.dirname(__file__)
    abs_file_path = os.path.join(base, user_prompt_file_name)
    
    # prompt creation logic 
    user_prompt = coverletter_structure+user_prompt+"## Job Description ##"
    # end of prompt creation logic
    open(abs_file_path,'w').write(user_prompt)