
from django.urls import path
from . import views
# start a coding
urlpatterns = [
    path("",views.index,name ="Shophome"),
    path("about/",views.about,name ="about"),
    path("contect/",views.contect,name ="contect"),
    path("tracker/",views.tracker,name ="tracker"),
    path("search/",views.search,name ="search"),
    path("productview/",views.productview,name ="productview"),
    path("checkout/",views.checkout,name ="checkout"),
]