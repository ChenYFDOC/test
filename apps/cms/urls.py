from django.urls import path
from . import views

app_name = 'cms'
urlpatterns = [
    path('', views.index, name='cms'),
    path('usermanager/', views.usermanager, name='usermanager'),
    path('role/', views.role, name='role'),
    path('permissions/',views.permissions,name='permissions')
]
