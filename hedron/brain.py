from colorama import Fore, Style
import colorama.ansi as ansi
from .models import TestModel
from django.conf import settings as s
import asyncio
import requests

from .scripts.loginManager import (commandToLogin as login,)


class HedronALX():
    def __init__(self):
        self.SESSION  = None
        self._PROMPT_ = ""
        self.__say__("\n" + s.LANGUAGE["WakingUP"], colour=Fore.CYAN, style=Style.BRIGHT)

        self.SESSION = requests.session()
        self.__say__(s.LANGUAGE["SessionCreated"], colour=Fore.CYAN, style=Style.BRIGHT)

    def __say__(self, message, colour: ansi.AnsiFore=Fore.WHITE, style: ansi.AnsiStyle=Style.NORMAL):
        print(colour + message + style)
        print(Style.RESET_ALL)

    def __help__(self):
        pass

    def loginMySelfIntoALXIntranet(self):
        self.__say__(s.LANGUAGE["TryingToLogIn"], colour=Fore.YELLOW)
        logginResult = asyncio.run(login(s.EMAIL, s.PASSWORD, s.ALX_URL,
                    s.ALX_PLANNING_PATH, s.ALX_AUTH_PATH, self.SESSION))
    
        if(logginResult[0] is False):
            self.__say__(s.LANGUAGE["CanNotLogin"] + " -> " + logginResult[1], colour=Fore.RED, style=Style.BRIGHT)
        else:
            self.__say__(s.LANGUAGE["LoggedInSuccessfully"], colour=Fore.GREEN, style=Style.BRIGHT)

    def prompt(self):
        self.__say__(f"[{s.LANGUAGE['self']} - 🤖] ->  {s.LANGUAGE['welcome']}")

        while self._PROMPT_ != "shutdown":
            self._PROMPT_ = str(input(f"[{s.LANGUAGE['self']} - 🤖]: "))

        
        self.__say__(f"[{s.LANGUAGE['self']} - 🤖] ->  {s.LANGUAGE['bye']}")

    def sleep(self):
        self.SESSION.close()


def brain(prompt:bool=False):
    me = HedronALX()
    me.loginMySelfIntoALXIntranet()
    if(prompt):
        me.prompt()
    me.sleep()