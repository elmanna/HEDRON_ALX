
# GOLBAL DEFINITIONS

TRANSLATION_ISO_CODE     = "" #pass it in command line
#or replace with your language iso code
USER_EMAIL               = "" # pass it in command line
#or replace with your alx account email address 
USER_PASSWORD            = "" # pass it in command line
#or replace with your alx account password 




def setupConfigurations(alx_email: str = "", alx_password: str = "", language_iso_code: str = "en"):
    global TRANSLATION_ISO_CODE, USER_EMAIL, USER_PASSWORD

    import django
    from pathlib import Path
    from django.conf import settings
    import json

    if settings.configured:
        return
    
    BASE_DIR                 = Path(__file__).resolve().parent.parent

    if(len(TRANSLATION_ISO_CODE) == 0):
        TRANSLATION_ISO_CODE = language_iso_code #pass it in command line
        #or replace with your language iso code

    if(len(USER_EMAIL) == 0):
        USER_EMAIL    = alx_email # pass it in command line
        #or replace with your alx account email address 
    if(len(USER_PASSWORD) == 0):
        USER_PASSWORD = alx_password # pass it in command line
        #or replace with your alx account password 
    try:
        LANGUAGE_FILE            = open(BASE_DIR / "settings" / f'translations/{TRANSLATION_ISO_CODE}.json')
    except Exception as e:
        LANGUAGE_FILE            = open(BASE_DIR / "settings" / f'translations/en.json')

    settings.configure(
        INSTALLED_APPS = ["hedron",],
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'database/db.sqlite3',
            },
        }, DEBUG=True,

        EMAIL               = USER_EMAIL, 
        PASSWORD            = USER_PASSWORD,

        ALX_URL             = "https://intranet.alxswe.com",
        
        ALX_PLANNING_PATH   = "/planning/me",
        ALX_AUTH_PATH       = "/auth/sign_in",

        TRANSLATION_ISO_CODE= TRANSLATION_ISO_CODE,

        LANGUAGE            = json.load(LANGUAGE_FILE)
    )

    LANGUAGE_FILE.close()


    django.setup()