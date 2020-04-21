from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("toSignUp", views.toSignUp_view, name="toSignUp"),
    path("signUp", views.signUp_view, name="signUp"),
    path("pizzaMenu", views.pizzaMenu_view, name="pizzaMenu"),
    path("pastaMenu", views.pastaMenu_view, name="pastaMenu"),
    path("subMenu", views.subMenu_view, name="subMenu"),
    path("saladMenu", views.saladMenu_view, name="saladMenu"),
    path("platterMenu", views.platterMenu_view, name="platterMenu")
]
