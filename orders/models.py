from django.db import models

# Create your models here.
class Pizza(models.Model):
    type = models.CharField(
    max_length = 8,
    choices = [('Sicilian', 'Sicilian'), ('Regular', 'Regular')],
    default='Regular',
    )
    TOPPINGS = (
    ('Pepperoni', 'Pepperoni'),
    ('Sausage', 'Sausage'),
    ('Mushrooms', 'Mushrooms'),
    ('Onions','Onions'),
    ('Ham','Ham'),
    ('Canadian Bacon','Canadian Bacon'),
    ('Pineapple','Pineapple'),
    ('Eggplant','Eggplant'),
    ('Tomato & Basil','Tomato & Basil'),
    ('Green Peppers','Green Peppers'),
    ('Hamburger','Hamburger'),
    ('Spinach','Spinach'),
    ('Artichoke', 'Artichoke'),
    ('Buffalo Chicken','Buffalo Chicken'),
    ('Barbecue Chicken','Barbecue Chicken'),
    ('Anchovies','Anchovies'),
    ('Black Olives','Black Olives'),
    ('Fresh Garlic','Fresh Garlic'),
    ('Zucchini','Zucchini'),
    ('None', 'None'),
    )

    topping1= models.CharField(
    max_length = 25,
    choices = TOPPINGS,
    default='None',
    )

    topping2= models.CharField(
    max_length = 25,
    choices = TOPPINGS,
    default='None',
    )

    topping3= models.CharField(
    max_length = 25,
    choices = TOPPINGS,
    default='None',
    )

    topping4= models.CharField(
    max_length = 25,
    choices = TOPPINGS,
    default='None',
    )

    topping5= models.CharField(
    max_length = 25,
    choices = TOPPINGS,
    default='None',
    )

    size = models.CharField(
    max_length = 5,
    choices = [('Small', 'Small'), ('Large', 'Large')],
    default = 'Small',
    )

class Sub(models.Model):
    SUBOPTIONS=(
    ('Cheese', 'Cheese'),
    ('Italian', 'Italian'),
    ('Ham + Cheese', 'Ham + Cheese'),
    ('Meatball', 'Meatball'),
    ('Tuna', 'Tuna'),
    ('Turkey', 'Turkey'),
    ('Chicken Parmigiana', 'Chicken Parmigiana'),
    ('Eggplant Parmigiana', 'Eggplant Parmigiana'),
    ('Steak', 'Steak'),
    ('Steak + Cheese', 'Steak + Cheese'),
    ('Sausage, Peppers & Onions', 'Sausage, Peppers & Onions'),
    ('Hamburger', 'Hamburger'),
    ('Cheeseburger', 'Cheeseburger'),
    ('Fried Chicken', 'Fried Chicken'),
    ('Veggie', 'Veggie'),
    )

    sub = models.CharField(
    max_length = 30,
    choices = SUBOPTIONS,
    default='Cheese',
    )

    addmushrooms = models.CharField(
    max_length = 3,
    choices = [('Yes', 'Yes'), ('No', 'No')],
    default='No',
    )

    addgreenpeppers = models.CharField(
    max_length = 3,
    choices = [('Yes', 'Yes'), ('No', 'No')],
    default='No',
    )

    addonions = models.CharField(
    max_length = 3,
    choices = [('Yes', 'Yes'), ('No', 'No')],
    default='No',
    )

    extracheese = models.CharField(
    max_length = 3,
    choices = [('Yes', 'Yes'), ('No', 'No')],
    default='No',
    )

class Salad(models.Model):
    SALADOPTIONS = (
    ('Garden Salad', 'Garden Salad'),
    ('Greek Salad', 'Greek Salad'),
    ('Antipasto', 'Antipasto'),
    ('Salad w/Tuna', 'Salad w/Tuna'),
    )

    salad = models.CharField(
    max_length = 15,
    choices=SALADOPTIONS,
    default='Garden Salad',
    )

class Pasta(models.Model):
    PASTAOPTIONS = (
    ('Baked Ziti w/Mozzarella', 'Baked Ziti w/Mozzarella'),
    ('Baked Ziti w/Meatballs', 'Baked Ziti w/Meatballs'),
    ('Baked Ziti w/Chicken', 'Baked Ziti w/Chicken'),
    )

    salad = models.CharField(
    max_length = 25,
    choices=PASTAOPTIONS,
    default='Baked Ziti w/Mozzarella',
    )

class DinnerPlatter(models.Model):
    PLATTEROPTIONS = (
    ('Garden Salad', 'Garden Salad'),
    ('Greek Salad', 'Greek Salad'),
    ('Antipasto', 'Antipasto'),
    ('Baked Ziti', 'Baked Ziti'),
    ('Meatball Parm', 'Meatball Parm'),
    ('Chicken Parm', 'Chicken Parm'),
    )

    salad = models.CharField(
    max_length = 20,
    choices=PLATTEROPTIONS,
    default='Baked Ziti',
    )
