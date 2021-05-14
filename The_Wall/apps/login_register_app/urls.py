from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('success/(<int:id>)', views.success, name="success"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('users/', views.users, name="users"),
    path('users/(<int:id>)/delete', views.delete_user, name="delete_user"),
    # path('registration', views.registration),
    # path('login', views.login),
    # # path('success$', views.success),
    # path('logout', views.logout),
]