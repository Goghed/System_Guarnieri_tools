from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastrar-usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastrar-cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
]

