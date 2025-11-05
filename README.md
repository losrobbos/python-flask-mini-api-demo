# Python API Mini Demo

This project uses the lib "Flask" to build a simple REST API

## Prep - create environment

Create a virtual environment where all packages, like Flask, will get installed to:

`python -m venv venv`

This command will create a folder "venv" in your folder, which will never get checked into github.

A Virtual environment is a way to install packages just on a project level, so just into your current project folder (=> venv) and not globally on your system.

## Activate Environment

Now first ACTIVATE this virtual environment:

Linux / Mac:
`source venv/Scripts/activate`

Windows:
`venv\Scripts/activate`

Now with the "venv" active, if you install any packages, they will get installed only locally into your folder.

## Install packages

Now install all package requirements, like Flask, for this project:

`pip install -r requirements.txt`

Now it should install Flask and all it's dependencies into your local "venv" folder.

You can check the installed packages:

`pip list --local`

It will just show the packages installed. for this project. Flask should be in that list, as well as some dependencies of Flask like "blinker".

## Start the API

Now run the project:

`python app.py`

It should start an API on http://127.0.0.1:5000

When you go there, you should see a welcome message.

By the way:
Also to START the app, you need the "venv" activates. Otherwises Python will look for the dependencies GLOBALLY on your system and will likely not find it there.
So always activate the venv before you start the project (see steps in "activate environment" above)

## Wenn Docker bei euch läuft

Image builden:
`docker build -t python-flask-demo .`

Container starten:
`docker run python-flask-demo`
