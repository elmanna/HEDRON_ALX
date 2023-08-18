


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{BASE_DIR}/settings/settings.py")
# django.setup()

def setupConfigurations():

    import django
    from pathlib import Path
    from django.conf import settings


    if settings.configured:
        return
    
    BASE_DIR = Path(__file__).resolve().parent.parent    

    settings.configure(
        INSTALLED_APPS = ["hedron",],
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'database/db.sqlite3',
            },
        }, DEBUG=True
    )

    django.setup()