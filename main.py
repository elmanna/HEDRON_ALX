from colorama import init, Fore, Style
from pathlib import Path
from settings.settings import setupConfigurations
from django.core.management import execute_from_command_line
import sys
import re

init()

BASE_DIR = Path(__file__).resolve().parent

def main():
    from hedron.brain import brain as wakeUp
    from django.conf import settings as s

    print(Fore.WHITE + s.LANGUAGE["wakeUpHedron"] + Style.BRIGHT)
    wakeUp()

def setup(flags: bool = False, alx_email: str = "", alx_password: str = "", language_iso_code: str = "en"):
    import settings.settings as sGlobal

    if(len(sGlobal.USER_EMAIL) == 0 or len(sGlobal.USER_PASSWORD) == 0):
        if not flags:
            print(
                 Fore.RED
                 + "Please define-in USER_EMAIL & USER_PASSWORD variables"
                 + "in settings.py file!\nor pass them directly using flags" 
                 + Style.BRIGHT)
            return
        setupConfigurations(alx_email=alx_email, alx_password=alx_password, language_iso_code=language_iso_code)
    else:
        setupConfigurations(language_iso_code=language_iso_code)

    # execute_from_command_line() # """ uncomment this line to 
    # to use the django command line (i.e manipulate DB & so on...) from within terminal"""
    main()


def helpMenu():
    print(
        Fore.WHITE
        + "\n[Flags]\n\n  --email [alx_email] \n  --password [alx_password]" 
        + "\n\n  --language [language_iso_code]"
        + "\n       available translations; [ Arabic (ar), English (en) ]"
        + Style.BRIGHT
    )
    exit(0)

def hedronCommandLine():
    alx_email: str                       = ""
    alx_password: str                    = ""
    language_iso_code: str               = ""
    crede_passby_command_line: bool = False
    abortFlag: bool                      = False

    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    for index, flag in enumerate(sys.argv):
        if flag.startswith("--h"):
            helpMenu()
        
        if flag == "--email":
            crede_passby_command_line = True
            try:
                if(re.match(email_regex, sys.argv[index+1])):
                    alx_email = sys.argv[index+1]
                    continue
                else:
                    print(Fore.RED + "\n[Error]\n\n Please enter [alx_email] in right format" + Style.BRIGHT)    
            except Exception as e:
                print(Fore.RED + "\n[Error]\n\n Please enter [alx_email] in right format" + Style.BRIGHT)
                abortFlag = True

        if flag == "--password":
            crede_passby_command_line = True
            try:
                if(sys.argv[index+1] != None):
                    alx_password = sys.argv[index+1]
                    continue
                else:
                    print(Fore.RED + "\n[Error]\n\n Please enter [alx_password] in right format" + Style.BRIGHT)
            except Exception as e:
                print(Fore.RED + "\n[Error]\n\n Please enter [alx_password] in right format" + Style.BRIGHT)
                abortFlag = True
        
        if flag == "--language":
            try:
                if(sys.argv[index+1] != None):
                    language_iso_code = sys.argv[index+1]
                    continue #left in case more flags added in the future
                else:
                    print(Fore.RED + "\n[Error]\n\n Please enter [language_iso_code] in right format" + Style.BRIGHT)    
            except Exception as e:
                print(Fore.RED + "\n[Error]\n\n Please enter [language_iso_code] in right format" + Style.BRIGHT)
                abortFlag = True

    if(abortFlag):
        helpMenu()

    if(crede_passby_command_line):
        if(len(alx_email) == 0 or len(alx_password) == 0):
            print(Fore.RED + "\n[HINT]\n\n  Please enter alx_email and alx_password." + Style.BRIGHT)
            abortFlag = True

    if(abortFlag):
        helpMenu()

    if(len(sys.argv) > 1):
        if(len(language_iso_code) > 0):
            setup(flags=True, alx_email=alx_email,
                   alx_password=alx_password, language_iso_code=language_iso_code)
        else:
            setup(flags=True, alx_email=alx_email, alx_password=alx_password)
    else:
        if(len(language_iso_code) > 0):
            setup(language_iso_code=language_iso_code)
        else:
            setup()

if __name__ == "__main__":
    hedronCommandLine()