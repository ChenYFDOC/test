from django.contrib import admin
from .models import LeftMenu,MenuClass

# Register your models here.
admin.site.register([LeftMenu,MenuClass])
