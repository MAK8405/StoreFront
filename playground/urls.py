from django.urls import path  # Path function
from . import views

# URLConf
urlpatterns = [path("hello/", views.sayHello)]
