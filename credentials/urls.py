from django.urls import path
from . import views

urlpatterns = [
    path("",views.signin),
    path("login/",views.login),
    path('main/',views.main),
    path('logout/',views.logout),
    path('inbox/',views.inbox),
    path('separate/',views.separate),

]