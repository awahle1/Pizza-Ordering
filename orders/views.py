from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
<<<<<<< HEAD
=======
from orders.models import Pizza
>>>>>>> parent of 29e7e98... All add to order buttons working

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "orders/pizza.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid Credentials"})

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
<<<<<<< HEAD
=======

def orderSicilian_view(request):
    size = request.POST["size"]
    topping1 = request.POST["topping1"]
    topping2 = request.POST["topping2"]
    topping3 = request.POST["topping3"]
    topping4 = request.POST["topping4"]
    topping5 = request.POST["topping5"]
    pizza = Pizza(type="Sicilian", topping1=topping1, topping2=topping2, topping3=topping3, topping4=topping4, topping5=topping5, size=size)
    pizza.save()
    return render(request, "orders/pizza.html")

def orderPizza_view(request):
    size = request.POST["size"]
    topping1 = request.POST["topping1"]
    print("---------------------------------------")
    print(size)
    print(topping1)
    return render(request, "orders/pizza.html")
>>>>>>> parent of 29e7e98... All add to order buttons working
