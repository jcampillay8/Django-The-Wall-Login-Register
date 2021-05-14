from django.urls import path
from . import views

urlpatterns = [
    # path('logout$', views.logout),
    # path('add_message$', views.add_message),
    path('/wall', views.wall),
    # path('comment/(?P<messageId>\d+)$', views.comment),
    # path('delete/(?P<messageId>\d+)$', views.delete),
]