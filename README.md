
Skip to content

    shreyas-bk24
    /
    MediKit

Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights

    Settings

Editing README.md in MediKit
Breadcrumbs

    MediKit

/
in
root

Indent mode
Indent size
Line wrap mode
Editing README.md file contents
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
# MediKit
An online Medical store with 3 level users [made up with FLASK]


## Directories and their Importance
The **MediKit** folder contains two folders and many py files,<br>
**TEMPLATES** folder contains all the html templates used for this project,<br>
**STATIC** this folder includes some other directories that have css,js,ajax and image files respectively.

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

### users
If you are a regular user or a customer you can login through the login button displayed on the nav bar<br>
>If you are a new user you can create account using sign up page after successfull sign up you are redirected into the address page,here you have to put the address of your home.</p>
 
### For_vendors <br>
>You can login by hovering the mouse on the medikit logo then you can find a link for login into the vendors account otherwise you can sign up into the account<br> vendors can add products to the database.

>**Note** <br> Admin dont have additional login page he will use the user login page to login the admin account.


## How to run
>**Warning** <br>To run this project you must have the latest version of python3


>**Warning** <br>Before installing we have to make sure that pip is already installed on your coding environment<br>

##
## setup pip


>To check pip is installed in your environment

```py 
pip --version 
Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
Attach files by dragging & dropping, selecting or pasting them.
Editing MediKit/README.md at root · shreyas-bk24/MediKit
