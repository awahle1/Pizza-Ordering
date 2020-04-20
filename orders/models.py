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
