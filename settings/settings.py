def setupConfigurations():

    import django
    from pathlib import Path
    from django.conf import settings
    import json


    if settings.configured:
        return
    
    BASE_DIR                 = Path(__file__).resolve().parent.parent

    TRANSLATION_ISO_CODE     = "ar"

    LANGUAGE_FILE            = open(BASE_DIR / "settings" / f'translations/{TRANSLATION_ISO_CODE}.json')

    USER_EMAIL    = "" # your alx account email address 
    USER_PASSWORD = "", # your alx account password 

    if(len(USER_EMAIL) == 0 or len(USER_PASSWORD) == 0):
        msg = json.load(LANGUAGE_FILE)["fillAccountCredentials"]
        raise ValueError(msg)

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

        LANGUAGE            = json.load(LANGUAGE_FILE)
    )

    LANGUAGE_FILE.close()

    django.setup()