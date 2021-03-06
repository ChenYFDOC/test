from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict

# Register your models here.

admin.site.site_header = '亿赛通超级管理员后台'
admin.site.site_title = '亿赛通超级管理员后台'


class ConfigAdmin(admin.ModelAdmin):
    exclude = ('id', 'created_by', 'groups', 'user_permissions')

    def save_model(self, request, obj, form, change):
        try:
            obj.created_by = request.user.username
            obj.save()
        except:
            obj.save()


class ConfigAdminForUser(ConfigAdmin):
    def save_model(self, request, obj, form, change):
        if obj.created_by:
            obj.created_by = request.user.username
        if change:
            get_user_model().objects.filter(username=obj.username).delete()
        get_user_model().objects.create_user(**model_to_dict(obj))


admin.site.register(User, ConfigAdminForUser)
admin.site.register(Group, ConfigAdmin)
admin.site.register(Permission, ConfigAdmin)
admin.site.register(Role, ConfigAdmin)
