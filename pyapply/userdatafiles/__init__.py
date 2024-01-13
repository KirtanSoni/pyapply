import json
import os

user_file_name = "user.json"
resume_file_name = "resume.txt"

## Config Structure ##
class Config:
    def __init__(self, api:str, path:str, name:str, address:str, email:str):
        '''Creates a config object with the given parameters'''
        self.api_key = api
        self.name = name
        self.address = address
        self.email = email
        self.path = path

    def dump(self,path:str):
        '''Dumps the config to a json file'''
        with open(path, 'w') as json_file:
            json.dump( {
                'OPEN_API_KEY': self.api_key,
                'name' : self.name,
                'address' : self.address,
                'email' : self.email,
                'path' : self.path,
            },json_file)
    



coverletter_structure = """Select 2 relevant Experiences and skills that match the requirements of the job description. 
Use selected items to write 4 paragraphs tailored to the job description, 3 sentences each, from the job description in 250 words
costraints: no Variables in Square brackets, avoid sentences that require extra information. extrapolate experience for unrelated jobs

Structure:
I am writing to express my interest on the given jobtitle...
Educational Background related paragraph...
Previous roles related paragraph...
Relevant Skills related to job descriptions....

Details:
"""



def load_user_data()->dict:
    '''Loads the user data from the user.json file
    or 
    raises an exception if the file is not found'''
    
    # internal absolute file path
    userdata_path = os.path.join(os.path.dirname(__file__), user_file_name)
    try:
        with open(userdata_path) as f:
            return json.load(f)
    except:
        raise Exception("User not Configured")


def load_coverletter_prompt()->str:
    '''Loads the resume and contructs prompt 
    or 
    raises an exception if the file is not found'''

    abs_file_path = os.path.join(os.path.dirname(__file__), resume_file_name)
    try:
        prompt = open(abs_file_path,'r').read()
        return coverletter_structure+prompt+"\n\nJob Description:"
    except Exception as e:
        raise Exception("Prompt not Configured")


def save_user_data(CONFIG:Config):
    base = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = os.path.join(base, user_file_name)
    CONFIG.dump(abs_file_path)


def save_resume(save_path):
    '''
    Saves the resume to the given path
    '''
    resume_path = os.path.join(os.path.dirname(__file__), resume_file_name)
    try:
        user_prompt = open(resume_path,'r').read()  #read resume
        abs_file_path = os.path.join(save_path, resume_file_name)
        open(abs_file_path,'w').write(user_prompt)
    except Exception as e:
        raise e


def config_prompt(path):
    try:
        user_prompt = open(path, 'r').read() 
    except Exception as e:
       raise e
    base = os.path.dirname(__file__)
    abs_file_path = os.path.join(base, resume_file_name)
    
    # prompt creation logic 
    # user_prompt = coverletter_structure+user_prompt+"## Job Description ##"
    # end of prompt creation logic
    open(abs_file_path,'w').write(user_prompt)