from django.contrib import admin
from .models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name','image')

admin.site.register(Customer,CustomerAdmin)