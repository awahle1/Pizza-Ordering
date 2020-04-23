from django.contrib import admin

from .models import Pizza
from .models import Sub
from .models import Pasta
from .models import Salad
from .models import DinnerPlatter
from .models import Order
# Register your models here.
admin.site.register(Pizza)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(Order)
