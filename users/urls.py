from django.urls import path
from .views import register_view, login_view, logout_view, user_list_view

urlpatterns = [
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('users/', user_list_view),
]