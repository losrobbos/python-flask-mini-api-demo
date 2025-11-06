# Python API Mini Demo

This project uses the lib "Flask" to build a simple REST API.

Flask is very similar to the package "express" in Node.

## Prep - create environment

After cloning this repository:
Create a virtual environment where all packages, like Flask, will get installed to:

`python -m venv venv`
(execute this command in the folder of the cloned repository, just like you would with "npm install")

This command will create a folder "venv" in your folder, which will never get checked into github.
(venv ist kind of like the "node_modules" folder in nodejs)

A Virtual environment is a way to install packages just on a project level, so just into your current project folder (=> venv) and not globally on your system.

## Activate Environment

Now first ACTIVATE this virtual environment (in the terminal):

Linux / Mac:
`source venv/Scripts/activate`

Windows:
`venv\Scripts\activate`

Now your terminal should always, after every command you type, e.g. "ls", print "(venv)" at the bottom, to assure you, you are in that virtual environment.

Now with the "venv" active, if you install any packages, they will get installed only locally into your folder.

## Install packages

Now install all package requirements, like Flask, for this project:

`pip install -r requirements.txt`

PIP is the Python Package Installer. Just like "npm" in Node.
And instead of a package.json file we got a plain textfile "requirements.txt" where all dependencies / needed packages are listed flat.

Now it should install Flask and all it's dependencies into your local "venv" folder.

You can check the installed packages:

`pip list --local`

It will just show the packages installed. for this project. Flask should be in that list, as well as some dependencies of Flask like "blinker".

## Start the API

Now run the project:

`python app.py`

It should start an API on http://127.0.0.1:8000

When you go there, you should see a welcome message.

By the way: Also to START the app, you need the "venv" activated. Not just during installation!

Otherwise Python will look for the dependencies GLOBALLY on your system and will likely not find it there.
So always activate the venv before you start the project (see steps in "activate environment" above)

## Start in Docker Container

Test if Docker is installed:
`docker --version`

Testen if Docker Engine is running:
`docker ps` // 

It should give an output like this:
```
$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
If an error occurs, the docker engine / daemon is not started.

Test a "Hello World" Container:
`docker run hello-world`

This command should print some (quite lengthy) hello world text into the terminal and then stop.

### Build Python App Docker Image

Execute this in the cloned repo folder
`docker build -t python-flask-demo .`

Start Container (Command -p allows that the INTERNAL Port 8000 in the container where our app runs also is opened on our LAPTOP, so the browser can reach it):
`docker run -p 8000:8000 python-flask-demo`

This way all traffic to "http://localhost:8000" that we enter into the browser, will get forwarded to the container app


