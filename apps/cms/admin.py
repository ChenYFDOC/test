from django.contrib import admin
from .models import LeftMenu, MenuClass


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'sort', 'url']


class StackInline(admin.StackedInline):
    model = LeftMenu


class ClassAdmin(admin.ModelAdmin):
    inlines = [StackInline]


admin.site.register(LeftMenu, MenuAdmin)
admin.site.register(MenuClass, ClassAdmin)
