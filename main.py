from colorama import init, Fore, Style
from pathlib import Path
from settings.settings import setupConfigurations
from hedron.brain import brain as wakeUp
from django.core.management import execute_from_command_line

init()

BASE_DIR = Path(__file__).resolve().parent

def main():
    from django.conf import settings as s

    print(Fore.WHITE + s.LANGUAGE["wakeUpHedron"] + Style.BRIGHT)
    wakeUp()

def setup():
    setupConfigurations()
    # execute_from_command_line() # """ uncomment this line to 
    # to use the django command line from within terminal"""
    main()

if __name__ == "__main__":
    setup()