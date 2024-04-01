from django.urls import path
from . import views


urlpatterns = [
    path('', views.UsersAPI.as_view(), name='users_api')
]