# MediKit
An online Medical store with 3 level users developed with FLASK

## Folder Details
The MediKit folder contains files the static files and templates required for this web application and the backend views

## Directories and their Importance
The *MediKit* folder contains two folders and many py files 
<b>TEMPLATES</b> folder contains all the html templates used for this project
<b>STATIC</b> this folder includes some other directories that have css,js,ajax and image files respectively

<h1>Python files description</h1>

run.py  - this file includes only the run config of the whole project its is the gateway of the web app.<br>
__init__.py - used to make the project behaves as a package.<br>
cart.py - includes views and routes related to the cart function.<br>
category.py - this file includes views of different categories.<br>
forgot_password.py  - As name suggests this file includes views only belongs to password rest functionality.<br>
routes.py - it contains views of the other functions like home,index etc.<br>
UserLogin.py  - it contains views about user functions.<br>
vendor.py - this file includes functions related to vendor (supplier).<br>

## How to use 
>users
If you are a regular user or a customer you can login through the login button displayed on the nav bar<br>
  If you are a new user you can create account using sign up page after successfull sign up you are redirected into the address page,here you have to put the address of your home.</p>
 
>For_vendors <br>
    You can login by hovering the mouse on the medikit logo then you can find a link for login into the vendors account otherwise you can sign up into the account

>Admin dont have additional login page he will use the user login page to logon the admin account


<h1>How to run</h1>
 To run this project you must have the latest version of python3
Firstly you have to install all the requirements mentioned in the requirements.txt<br>
>**Note** Before installing we have to make sure that pip is already installed on your coding environment<br>

>To check pip is installed in your environment

```py 
pip --version 
```

>if no pip version detected.Install pip using this command


>for windows

```py
py get-pip.py
```

>for linux and mac users

```py
python get-pip.py
```

>updating pip 

>for windows
```py
py -m pip install --upgrade pip
```

>for linux and mac
```py
python -m pip install --upgrade pip
```

>Set up environment and run the server

>creating a virtual env
```py
python3 -m venv env
```

>activating virtual env
```bash
source env/bin/activate
```
>installing the required packages using requirements.txt
```py
pip3 install -r requirements.txt
```
>configure the server and run the application

```shell
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

<h4>developed and tested with the colabaration of
<br>Team MediKit</h4>




