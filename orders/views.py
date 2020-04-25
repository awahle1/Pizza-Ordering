from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from orders.models import Pizza, Sub, Salad, Pasta, DinnerPlatter, Order, CompleteOrder

# Create your views here.
currentorder = 0
user = None

def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user
    }
    global user
    user = request.user
    if Order.objects.get(userid = user.id) is None:
        order = Order(userid = user.id)
        order.save()
    else:
        return render(request, "orders/choose.html")
    return render(request, "orders/pizza.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    global user
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid Credentials"})

def yes_view(request):
    global currentorder
    currentorder = Order.objects.get(userid = user.id).id
    return render(request, "orders/pizza.html")

def no_view(request):
    order = Order(userid = user.id)
    order.save()
    global currentorder
    currentorder = order.id
    return render(request, "orders/pizza.html")

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def toSignUp_view(request):
    return render(request, "orders/signup.html")

def signUp_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    firstname = request.POST["firstName"]
    lastname = request.POST["lastName"]
    user = authenticate(request, username=username, password=password)
    if user is None:
        if username is not None and password is not None and email is not None and firstname is not None and lastname is not None:
            newuser = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=firstname,
            last_name=lastname)
            user = authenticate(request, username=username, password=password)
            login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/signup.html", {"message": "Username already in use"})

def pizzaMenu_view(request):
    return render(request, "orders/pizza.html")

def subMenu_view(request):
    return render(request, "orders/subs.html")

def pastaMenu_view(request):
    return render(request, "orders/pasta.html")

def saladMenu_view(request):
    return render(request, "orders/salads.html")

def platterMenu_view(request):
    return render(request, "orders/platters.html")

def orderSicilian_view(request):
    size = request.POST["size"]
    topping1 = request.POST["topping1"]
    topping2 = request.POST["topping2"]
    topping3 = request.POST["topping3"]
    topping4 = request.POST["topping4"]
    topping5 = request.POST["topping5"]
    pizza = Pizza(type="Sicilian", topping1=topping1, topping2=topping2, topping3=topping3, topping4=topping4, topping5=topping5, size=size)
    pizza.save()
    order = Order.objects.get(pk=currentorder)
    order.pizza.add(pizza)
    return HttpResponseRedirect(reverse("cart", args=()))

def orderPizza_view(request):
    size = request.POST["size"]
    topping1 = request.POST["topping1"]
    topping2 = request.POST["topping2"]
    topping3 = request.POST["topping3"]
    topping4 = request.POST["topping4"]
    topping5 = request.POST["topping5"]
    pizza = Pizza(type="Regular", topping1=topping1, topping2=topping2, topping3=topping3, topping4=topping4, topping5=topping5, size=size)
    pizza.save()
    order = Order.objects.get(pk=currentorder)
    order.pizza.add(pizza)
    context = {
        "order": order
    }
    return HttpResponseRedirect(reverse("cart", args=()))

def orderSub_view(request):
    size = request.POST["size"]
    sub = request.POST["sub"]
    mushrooms = request.POST["mushrooms"]
    greenpeppers = request.POST["greenpeppers"]
    onions = request.POST["onions"]
    xtracheese = request.POST["xtracheese"]
    sub = Sub(sub=sub, addmushrooms=mushrooms, addgreenpeppers=greenpeppers, addonions=onions, extracheese=xtracheese, size=size)
    sub.save()
    order = Order.objects.get(pk=currentorder)
    order.subs.add(sub)
    return HttpResponseRedirect(reverse("cart", args=()))

def orderPasta_view(request):
    pasta = request.POST["pasta"]
    past = Pasta(pasta=pasta)
    past.save()
    order = Order.objects.get(pk=currentorder)
    order.pasta.add(past)
    return HttpResponseRedirect(reverse("cart", args=()))

def orderSalad_view(request):
    salad = request.POST["salad"]
    sal = Salad(salad=salad)
    sal.save()
    order = Order.objects.get(pk=currentorder)
    order.salads.add(sal)
    return HttpResponseRedirect(reverse("cart", args=()))

def orderPlatter_view(request):
    size = request.POST["size"]
    platter = request.POST["platter"]
    plat = DinnerPlatter(size=size, platter=platter)
    plat.save()
    print("---------------------------------")
    order = Order.objects.get(pk=currentorder)
    order.platters.add(plat)
    return HttpResponseRedirect(reverse("cart", args=()))

def cart_view(request):
    order = Order.objects.get(pk=currentorder)
    price = order.getprice()
    context = {
        "order": order,
        "price": price
    }
    return render(request, "orders/cart.html", context)

def place(request):
    order = Order.objects.get(pk=currentorder)
    pizzalist = ""
    for pizza in order.pizza.all():
        if pizzalist == "":
            pizzalist = pizza
        else:
            pizzalist = str(pizzalist) + ", " + str(pizza)
    sublist = ""
    for sub in order.subs.all():
        if sublist == "":
            sublist = sub
        else:
            sublist = str(sublist) + ", " + str(sub)
    saladlist = ""
    for salad in order.salads.all():
        if saladlist == "":
            saladlist = salad
        else:
            saladlist = str(saladlist) + ", " + str(salad)
    pastalist = ""
    for pasta in order.pasta.all():
        if pastalist == "":
            pastalist = pasta
        else:
            pastalist = str(pastalist) + ", " + str(pasta)
    platterlist = ""
    for platter in order.platters.all():
        if platterlist == "":
            platterlist = platter
        else:
            platterlist = str(platterlist) + ", " + str(platter)
    placeorder = CompleteOrder(pizzas = pizzalist, salads = saladlist, pastas = pastalist, platters = platterlist, subs = sublist, userid=order.userid, price = order.getprice())
    placeorder.save()
    price = order.getprice()
    context = {
        "order": order,
        "price": price
    }
    return render(request, "orders/complete.html", context)
