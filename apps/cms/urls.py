from django.urls import path
from . import views

app_name = 'cms'
urlpatterns = [
    path('', views.users.index, name='cms'),
    path('usermanager/', views.users.usermanager, name='usermanager'),
    path('role/', views.users.role, name='role'),
    path('permissions/', views.users.permissions, name='permissions'),
    path('key_type/', views.license.key_type, name='key_type')
]
