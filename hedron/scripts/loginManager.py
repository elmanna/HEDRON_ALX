from colorama import Fore, Style
from bs4 import BeautifulSoup 
import asyncio
import json

def amILoggedIn(alx_planning_url, SESSION) -> bool:
    response = SESSION.request(method="get", url=alx_planning_url, allow_redirects=False)
    if(response.status_code == 200):
        # html     = BeautifulSoup(response.content, "html.parser")
        # tag    = html.find("a", {"href": "/users/my_profile"}).find("div", {"class": "inner"}).attrs["style"]
        # # style    = soup.find("div", title="My Profile") #.find("a").find("div").find("div")["style"]
        # print(tag)
        return True
    
    return False

async def login(email, password, alx_auth_url, SESSION) -> bool:
    
    response_text = SESSION.get(alx_auth_url).text #first fetch page to get new authenticity token
    html          = BeautifulSoup(response_text, "html.parser")
    token         = html.find("input", {"name": "authenticity_token"}).attrs["value"] 

    payload       = {
        "authenticity_token": token,
        "user[email]": email,
        "user[password]": password,
        "user[remember_me]": 0,
        "commit": "Log in"
    }

    response = SESSION.request(method="post", url=alx_auth_url, data=payload)

    if(response.status_code == 200):
        return True

    return False

async def commandToLogin(email, password, alx_url,
                          alx_planning_path, alx_auth_path, SESSION) -> bool:
    try:
        isLoggedIn = amILoggedIn(alx_url + alx_planning_path, SESSION)
        while isLoggedIn == False:
           await login(email, password, alx_url + alx_auth_path, SESSION)
           isLoggedIn = amILoggedIn(alx_url + alx_planning_path, SESSION)
           
    except Exception as e:
        return [False, e.__str__()]
    return [True, None]