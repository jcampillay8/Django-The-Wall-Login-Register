from django.urls import path
from . import views

urlpatterns = [
    path('thewall/logout', views.logout),
    path('thewall/add_message', views.add_message),
    path('thewall/wall', views.wall),
    path('thewall/comment/(<int:messageId>)', views.comment),
    path('thewall/delete/(<int:messageId>)', views.delete),
]