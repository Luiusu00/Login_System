from django.urls import path
from . import views

urlpatterns = [
    path('', views.telaLogin, name='telaLogin'),
    path('sistema/', views.sistema, name='sistema'),
    path('new-password/', views.newPassword, name='new-password'),
    path('logout/', views.logout, name='logout'),

]
