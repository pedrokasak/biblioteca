from django.urls import path
from . import views

app_name='pages'

urlpatterns = [
    path('', views.LoginPageView.as_view(), name='login')
]