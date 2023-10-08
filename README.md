![example workflow](https://github.com/reproductionprohibited/url_shortener_django/actions/workflows/django.yml/badge.svg?event=push)

# URL SHORTENER DJANGO

! Disclaimer: All the next commands are meant to be applied on a MacOS/Linux system. Use google to find their Windows alternatives !

## Setting up Virtual Environment ( venv )

In order to create virtual environment (venv) folder, you have to clone the repo, and then with terminal go to the
root folder and type in the next command:

```
python3 -m venv <title>
```

You can type in any folder name you want instead of <title> in the command

Then you should activate the venv:

```
source <title>/bin/activate
```

After that in the beginning of every terminal line you should see a (venv) prefix

In order to deactivate the venv just use this command:

```
deactivate
```

## Dev-mode launch

To launch the project in dev mode, follow the previous steps, and then use:
```
pip3 install -r requirements.txt
```
This will install all necessary requirements for the project

Then run manage.py file
```
cd url_shortener_django

python3 manage.py runserver
```
Go to 127.0.0.1:8000. There you will see the site


## .env constants

Create a .env file in the root project folder and set values to next constants:

1) DEBUG ( bool: True/False )

2) SECRET_KEY ( str: Django secret key)

3) ALLOWED_HOSTS ( List[str]: list of allowed hosts)
