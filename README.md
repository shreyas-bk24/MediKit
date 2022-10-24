# MediKit
An online Medical store with 3 level users developed with FLASK

<h1>Directories and their Importance</h1>
The <b>MediKit</b> folder contains two folders and many py files 
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

<h1>How to use <h1>
 <p>If you are a regular user or a customer you can login through the login button displayed on the nav bar<br>
  If you are a new user you can create account using sign up page after successfull sign up you are redirected into the address page,here you have to put the address of your home.</p>
  <br>
  <h3>For vendors /Suppliers<h3>
    You can login by hovering the mouse on the medikit logo then you can find a link for login into the vendors account otherwise you can sign up into the account<br>
<h3>Admin</h3 dont have additional login page he'll use the user login page to logon the admin account
