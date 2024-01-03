# author : Kirtan Soni

import pyperclip
from pyapply.workflows.asujobs import asujobs
import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
from .userdatafiles import save_user_data, config_prompt, load_user_data, load_coverletter_prompt,Config
from .utils import listener, requestgpt


VERSION = "0.1"

@click.group(
    cls=HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='green'
)
def cli():
    pass

@cli.command(help="Starts the listener")
def listen():

    click.echo(click.style(f"Listening for job descriptions...", fg="green"))
    try:
        load_user_data(), load_coverletter_prompt()
        listener(3,pyperclip.paste ,asujobs)
    except Exception as e:
        click.echo(click.style(f"{e}", fg="red"))
        return


@click.command(help="set reference resume for cover letter generation (persistent)")
@click.argument('resume_path', type=click.Path(exists=True, resolve_path=True))
def set_resume(resume_path):

    try:
        config_prompt(resume_path)
        click.echo(click.style(f"Resume configured.", fg="green"))
    except Exception as e:
        click.echo(click.style(f"{e}", fg="red"))


@click.command(help="set user data for cover letter generation (persistent)")
@click.argument('save_path', type=click.Path(exists=True, resolve_path=True))
def set_user(save_path):

    api = click.prompt(click.style(f"Enter your OPENAI API KEY", fg="yellow"))
    name = click.prompt(click.style(f"Enter your Full Name", fg="yellow"))
    address = click.prompt(click.style("Enter your City, State", fg="yellow"))
    email = click.prompt(click.style("Enter your Email", fg="yellow"))
    path = save_path
    user = Config(
        path= path,
        api= api,
        name= name,
        address= address,
        email= email,
    )
    save_user_data(user)   
    try:
        test = requestgpt("write"+name+" a greeting for the day") #TODO: rethink this.
        click.echo(click.style(f"{test}", fg="green"))
    except Exception as e:
        click.echo(click.style(f"{e}", fg="red"))
        return
    click.echo(click.style(f"User data configured.", fg="green"))


@click.command(help="About PyApply")
def about():

    click.echo("-------------------------------------------")
    click.echo(click.style(f"PyApply :", fg="magenta")+click.style(f": https://github.com/kirtansoni/pyapply", fg="cyan"))
    click.echo("-------------------------------------------")
    click.echo(click.style(f"- CLI tool to automate the process of applying to jobs.", fg="green"))
    click.echo(click.style(f"- Currently only supports Asu Student jobs", fg="green"))
    click.echo(click.style(f"- Open source and free to use", fg="green"))
    click.echo(click.style(f"- Built by Kirtan Soni", fg="green"))
    click.echo("-------------------------------------------")
    click.echo(click.style(f"Feedback", fg="yellow")+click.style(f": https://github.com/kirtansoni/pyapply/issues", fg="cyan"))
    click.echo(click.style(f"Version ", fg="yellow")+click.style(f"{VERSION}", fg="green"))
    click.echo(click.style(f"Requirements ", fg="yellow")+click.style(f"CHATGPT 3.5 API Key", fg="green"))


cli.add_command(listen)
cli.add_command(set_user)
cli.add_command(set_resume)
cli.add_command(about)


if __name__ == "__main__":
    cli()
