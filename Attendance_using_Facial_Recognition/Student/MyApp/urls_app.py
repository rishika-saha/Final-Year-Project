from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="Login"),
    path('capture_image', views.capture_image, name="Capture_Image"),
    path('result', views.fetch_compare, name="Results"),
]
