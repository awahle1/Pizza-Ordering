# Project 3

Web Programming with Python and JavaScript

This project is a website for Pinocchio's pizza, a pizza restaurant in Cambridge, MA. It allows customers to make accounts, browse the menu, and place orders.  

styles.css - contains all of the css for the Project

templates folder - contains many templates with mostly self explanatory names, however I will explain the less obvious ones

base.html - this file contains all of the head information for all of the html files and all other templates are children of this.

user.html - this file contains the bar that allows users to navigate the menu as well as logout and go to the cart. It is the parent to all of the templates that are named after foods.

{{food}}.html - this file contains the menu information for {{food}} and allows users to order {{food}}

choose.html - this is what renders the page that asks users coming back to the site whether or not they want to continue the order that they were previously making.

complete.html - this file renders the page that is shown after a user submits their order

admin.py - this file allows me to manage which models are shown in the admin interface and which are not

models.py - this file is where I wrote all of the classes that correspond to tables in the database. This includes all of the menu items and orders.

urls.py - this file contains all of the routes for the whole app. It directs users from a link to a corresponding function in views.py

views.py - this file is essentially the brains of the app. This is what decides what to do whenever the user interacts with the webpage.  
