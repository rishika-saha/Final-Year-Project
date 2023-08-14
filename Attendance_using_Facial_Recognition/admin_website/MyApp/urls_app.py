from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='Home'),
    path('upload', views.upload, name='Upload'),
    path('success', views.success, name='Success'),
    path('logout', views.logout_user, name='Logout')
]