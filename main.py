# import os, django
from pathlib import Path
from settings.settings import setupConfigurations
from hedron.brain import init
from django.core.management import execute_from_command_line

BASE_DIR = Path(__file__).resolve().parent

def main():
    init()

def setup():
    setupConfigurations()
    execute_from_command_line()
    main()

if __name__ == "__main__":
    setup()