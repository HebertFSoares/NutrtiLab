from unicodedata import name
from django.urls import URLPattern, path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name="logar"), 
    path('sair/', views.sair, name="sair"),  
    path('ativar_conta/<str:token>/', views.ativar_conta, name="ativar_conta"),
]
