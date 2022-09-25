from django.contrib import admin
from django.urls import path
from . import views
# start a coding
urlpatterns = [
    path("",views.index,name ="bloghome")
]