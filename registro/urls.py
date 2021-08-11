from django.urls import path
from .views import *

urlpatterns = [
    path('', registro, name='registro'),
    path('listado', listado_registro, name='listado_registro'),
    path('export', listado_export, name='listado_export'),



    #Auth
    path('signup/', signupuser, name="signupuser"),
    path('logout/', logoutuser, name="logoutuser"),
    path('login/', loginuser, name="loginuser"),

    ]