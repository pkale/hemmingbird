from django.contrib import admin

# Register your models here.
from .models import Songs, Customer, Tailor, Order

admin.site.register(Customer)
admin.site.register(Tailor)
admin.site.register(Order)