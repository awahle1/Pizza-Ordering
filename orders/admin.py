from django.contrib import admin

from .models import Pizza, Sub, Pasta, Salad, DinnerPlatter, Order, CompleteOrder

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(Order)
admin.site.register(CompleteOrder)
