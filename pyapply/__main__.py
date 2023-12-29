# author : Kirtan Soni
import pyperclip
import os
from pyapply.app   import listener
from pyapply.workflows.asujobs import asujobs
import click
from .utils import requestgpt

prompt_path = "pyapply/prompts"

@click.group()
def cli():
    pass

@cli.command()
def listen():
    print("Starting listener...")
    listener(3,pyperclip.paste ,asujobs)


@click.command()
def set_user():
    api = click.prompt("Enter your openai api key")
    name = click.prompt("Enter your name")
    address = click.prompt("Enter City, State")
    email = click.prompt("Enter your email")
    path = click.prompt("Enter your saving dir")
    resume_path = click.prompt("Enter your resume textfile path")
    resume = open(resume_path, "r").read()

    final_prompt = open(prompt_path+"/template.txt",'r').read()
    final_prompt += resume
    open(prompt_path+"/coverletter.txt",'w').write(final_prompt)

    applied_path = path + "/History"
    user = {
        'OPEN_API_KEY': api,
        'name' : name,
        'address' : address,
        'email' : email,
        'path' : path,
        'history_path' : applied_path,
        'prompt_path': prompt_path,
    }
    print(user+"\n"+final_prompt)


cli.add_command(listen)
cli.add_command(set_user)


if __name__ == "__main__":
    try:
        os.environ["OPENAI_API_KEY"]
    except Exception as e:
        print(f"Error: export OPENAI_API_KEY=<your-key>")
        exit(1)
    print("Author Kirtan Soni")
    cli()
