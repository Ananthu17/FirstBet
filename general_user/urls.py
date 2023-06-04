from django.urls import path
from .views import Home_view, Login_view


urlpatterns = [
    path('', Home_view.as_view(), name="home"),
    path('login', Login_view.as_view(), name="login")
]
