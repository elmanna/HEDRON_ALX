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
        
        self.__say__(s.LANGUAGE["WakingUP"], colour=Fore.CYAN, style=Style.BRIGHT)

        self.SESSION = requests.session()
        self.__say__(s.LANGUAGE["SessionCreated"], colour=Fore.CYAN, style=Style.BRIGHT)

    def __say__(self, message, colour: ansi.AnsiFore=Fore.WHITE, style: ansi.AnsiStyle=Style.NORMAL):
        print(colour + message + style)

    def loginMySelfIntoALXIntranet(self):
        self.__say__(s.LANGUAGE["TryingToLogIn"], colour=Fore.YELLOW)
        logginResult = asyncio.run(login(s.EMAIL, s.PASSWORD, s.ALX_URL,
                    s.ALX_PLANNING_PATH, s.ALX_AUTH_PATH, self.SESSION))
    
        if(logginResult[0] is False):
            self.__say__(s.LANGUAGE["CanNotLogin"] + " -> " + logginResult[1], colour=Fore.RED, style=Style.BRIGHT)
        else:
            self.__say__(s.LANGUAGE["LoggedInSuccessfully"], colour=Fore.GREEN, style=Style.BRIGHT)


def brain():
    me = HedronALX()
    me.loginMySelfIntoALXIntranet()