from django.contrib import admin
from .models import MyModel, Order


# Register your models here.
admin.site.register(MyModel)
admin.site.register(Order)
