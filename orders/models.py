from django.db import models
from django.contrib.auth.models import User

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

    def getprice(self):
        price = 0.0
        numtoppings = 0
        if self.topping1 != " ":
            numtoppings += 1
        if self.topping2 != " ":
            numtoppings += 1
        if self.topping3 != " ":
            numtoppings += 1
        if self.topping4 != " ":
            numtoppings += 1
        if self.topping5 != " ":
            numtoppings += 1
        if self.type=="Regular":
            if self.size=="Large":
                if numtoppings==0:
                    price = 17.95
                if numtoppings==1:
                    price = 19.95
                if numtoppings==2:
                    price = 21.95
                if numtoppings==3:
                    price = 23.95
                if numtoppings>=4:
                    price = 25.95
            if self.size=="Small":
                if numtoppings==0:
                    price = 12.70
                if numtoppings==1:
                    price = 13.70
                if numtoppings==2:
                    price = 15.20
                if numtoppings==3:
                    price = 16.20
                if numtoppings>=4:
                    price = 17.75
        if self.type=="Sicilian":
            if self.size=="Small":
                if numtoppings==0:
                    price = 24.45
                if numtoppings==1:
                    price = 26.45
                if numtoppings==2:
                    price = 28.45
                if numtoppings==3:
                    price = 29.45
                if numtoppings>=4:
                    price = 30.45
            if self.size=="Large":
                if numtoppings==0:
                    price = 38.70
                if numtoppings==1:
                    price = 40.70
                if numtoppings==2:
                    price = 42.70
                if numtoppings==3:
                    price = 44.70
                if numtoppings>=4:
                    price = 45.70
        return(price)
    def __str__(self):
        numtoppings = 0
        if self.topping1 != " ":
            numtoppings += 1
        if self.topping2 != " ":
            numtoppings += 1
        if self.topping3 != " ":
            numtoppings += 1
        if self.topping4 != " ":
            numtoppings += 1
        if self.topping5 != " ":
            numtoppings += 1
        if numtoppings == 5:
            return str("{} {} Pizza with {}, {}, {}, {}, and {}").format(self.size, self.type, self.topping1, self.topping2, self.topping3, self.topping4, self.topping5)
        if numtoppings == 4:
            return str("{} {} Pizza with {}, {}, {}, and {}").format(self.size, self.type, self.topping1, self.topping2, self.topping3, self.topping4)
        if numtoppings == 3:
            return str("{} {} Pizza with {}, {}, and {}").format(self.size, self.type, self.topping1, self.topping2, self.topping3)
        if numtoppings == 2:
            return str("{} {} Pizza with {}, and {}").format(self.size, self.type, self.topping1, self.topping2)
        if numtoppings == 1:
            return str("{} {} Pizza with {}").format(self.size, self.type, self.topping1)
        if numtoppings == 0:
            return str("{} {} Cheese Pizza").format(self.size, self.type)

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
    size = models.CharField(
    max_length = 5,
    choices = [('Small', 'Small'), ('Large', 'Large')],
    default = 'Small',
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
    def getprice(self):
        price = 0.0
        if self.sub == "Cheese" or self.sub == "Italian" or self.sub == "Ham + Cheese" or self.sub == "Meatball" or self.sub == "Tuna" or self.sub == "Eggplant Parmigiana" or self.sub == "Steak":
            if self.size == "Small":
                price = 6.50
            if self.size == "Large":
                price = 7.95
        if self.sub == "Turkey" or self.sub == "Chicken Parmigiana":
            if self.size == "Small":
                price = 7.50
            if self.size == "Large":
                price = 8.50
        if self.sub == "Steak + Cheese" or self.sub == "Fried Chicken" or self.sub == "Veggie" or self.sub == "Sausage, Peppers & Onions":
            if self.size == "Small":
                price = 6.95
            if self.size == "Large":
                price = 8.50
        if self.sub == "Hamburger":
            if self.size == "Small":
                price = 4.60
            if self.size == "Large":
                price = 6.95
        if self.sub == "Cheeseburger":
            if self.size == "Small":
                price = 5.10
            if self.size == "Large":
                price = 7.45
        if self.addmushrooms == "Yes":
            price += 0.50
        if self.addonions == "Yes":
            price += 0.50
        if self.addgreenpeppers == "Yes":
            price += 0.50
        if self.extracheese == "Yes":
            price += 0.50
        return(price)
    def __str__(self):
        substr = str("{} {} Sub".format(self.size, self.sub))
        if self.addmushrooms == "Yes" or self.addonions == "Yes" or self.addgreenpeppers == "Yes" or self.extracheese == "Yes":
            substr = substr + " with "
        if self.addmushrooms == "Yes":
            substr = substr + "mushrooms "
        if self.addonions == "Yes":
            substr = substr + "onions "
        if self.addgreenpeppers == "Yes":
            substr = substr + "green peppers "
        if self.extracheese == "Yes":
            substr = substr + "extra cheese"
        return substr

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
    def getprice(self):
        price = 0.0
        if self.salad == "Garden Salad":
            price = 6.25
        if self.salad == "Greek Salad" or self.salad == "Antipasto" or self.salad == "Salad w/Tuna":
            price = 8.25
        return (price)
    def __str__(self):
        return("{}").format(self.salad)

class Pasta(models.Model):
    PASTAOPTIONS = (
    ('Baked Ziti w/Mozzarella', 'Baked Ziti w/Mozzarella'),
    ('Baked Ziti w/Meatballs', 'Baked Ziti w/Meatballs'),
    ('Baked Ziti w/Chicken', 'Baked Ziti w/Chicken'),
    )

    pasta = models.CharField(
    max_length = 25,
    choices=PASTAOPTIONS,
    default='Baked Ziti w/Mozzarella',
    )
    def getprice(self):
        price = 0.0
        if self.pasta == "Baked Ziti w/Mozzarella":
            price = 6.50
        if self.pasta == "Baked Ziti w/Meatballs":
            price = 8.75
        if self.pasta == "Baked Ziti w/Chicken":
            price = 9.75
        return(price)
    def __str__(self):
        return("{}").format(self.pasta)

class DinnerPlatter(models.Model):
    PLATTEROPTIONS = (
    ('Garden Salad', 'Garden Salad'),
    ('Greek Salad', 'Greek Salad'),
    ('Antipasto', 'Antipasto'),
    ('Baked Ziti', 'Baked Ziti'),
    ('Meatball Parm', 'Meatball Parm'),
    ('Chicken Parm', 'Chicken Parm'),
    )

    platter = models.CharField(
    max_length = 20,
    choices=PLATTEROPTIONS,
    default='Baked Ziti',
    )

    size = models.CharField(
    max_length = 5,
    choices = [('Small', 'Small'), ('Large', 'Large')],
    default = 'Small',
    )
    def getprice(self):
        price = 0.0
        if self.size == "Small":
            if self.platter == "Greek Salad" or self.platter == "Antipasto" or self.platter == "Meatball Parm":
                price = 50.0
            if self.platter == "Garden Salad" or self.platter == "Baked Ziti":
                price = 40.0
            if self.platter == "Chicken Parm":
                price = 55.0
        if self.size == "Large":
            if self.platter == "Greek Salad" or self.platter == "Antipasto" or self.platter == "Meatball Parm":
                price = 75.0
            if self.platter == "Garden Salad" or self.platter == "Baked Ziti":
                price = 65.0
            if self.platter == "Chicken Parm":
                price = 85.0
        return (price)
    def __str__(self):
        return("{} {} Platter").format(self.size, self.platter)

class Order(models.Model):
    pizza = models.ManyToManyField(Pizza, related_name="pizzas")
    salads = models.ManyToManyField(Salad, related_name="salads")
    subs = models.ManyToManyField(Sub, related_name="subs")
    platters = models.ManyToManyField(DinnerPlatter, related_name="platters")
    pasta = models.ManyToManyField(Pasta, related_name="pastas")
    userid = models.IntegerField(
        default = 0
    )

    def getprice(self):
        pizzaprice = 0
        platterprice = 0
        subprice = 0
        pastaprice = 0
        saladprice = 0
        for za in self.pizza.all():
            pizzaprice += za.getprice()
        for platter in self.platters.all():
            platterprice += platter.getprice()
        for sub in self.subs.all():
            subprice += sub.getprice()
        for sta in self.pasta.all():
            pastaprice += sta.getprice()
        for salad in self.salads.all():
            saladprice += salad.getprice()
        totalprice = pizzaprice + saladprice + subprice + pastaprice + platterprice
        return("$" +"%.2f" % totalprice)

    def __str__(self):
        return("Order {}").format(self.id)

class CompleteOrder(models.Model):
    pizzas = models.CharField(
        max_length=10000,
        default = "",
        blank=True,
        null=True
    )
    salads = models.CharField(
        max_length=10000,
        default = "",
        blank=True,
        null=True
    )
    pastas = models.CharField(
        max_length=10000,
        default = "",
        blank=True,
        null=True
    )
    platters = models.CharField(
        max_length=10000,
        default = "",
        blank=True,
        null=True
    )
    subs = models.CharField(
        max_length=10000,
        default = "",
        blank=True,
        null=True
    )
    userid = models.IntegerField(
        default = 0
    )
    price = models.CharField(
        max_length = 10,
        default = "$0",
    )
    status = models.CharField(
        max_length=20,
        default = "Received",
        choices = [('Received', 'Received'), ('In Progress', 'In Progress'), ('Complete', 'Complete')]
    )
    def __str__(self):
        return("Order {}").format(self.id)
