# author : Kirtan Soni

import time
import pyperclip
import os
from pyapply.workflows.asujobs import asujobs
import click
from .userdatafiles import load_user_data, save_user_data, load_coverletter_prompt, config_prompt






def listener(interval: int, inputcallback, callback) -> None:
    try:
        load_user_data()
        load_coverletter_prompt()
    except Exception as e:
        print(e)
        exit(1)
    clipboard = inputcallback()
    while True:
        if clipboard == inputcallback():
            continue
        clipboard = inputcallback()
        try:
            callback(clipboard)
        except Exception as e:
            print(f"Error in listener: {e}")
            continue
        time.sleep(interval)



prompt_path = "pyapply/prompts"

@click.group()
def cli():
    pass



@cli.command()
def listen():
    print("Starting listener...")
    listener(3,pyperclip.paste ,asujobs)


@click.command()
@click.argument('resume_path', type=click.Path(exists=True, resolve_path=True))
def set_resume(resume_path):
    config_prompt(resume_path)
    


@click.command()
@click.argument('save_path', type=click.Path(exists=True, resolve_path=True))
def set_user(save_path):
    api = click.prompt("openai api key: ")
    name = click.prompt("name: ")
    address = click.prompt("city, State: ")
    email = click.prompt("email: ")
    path = save_path
    # create user.json
    user = {
        'OPEN_API_KEY': api,
        'name' : name,
        'address' : address,
        'email' : email,
        'path' : path,
    }
    save_user_data(user)   

cli.add_command(listen)
cli.add_command(set_user)
cli.add_command(set_resume)

if __name__ == "__main__":
    print("Author Kirtan Soni")
    cli()
