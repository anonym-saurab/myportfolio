from django.urls import path
from portfolio import views

## creating urls here

urlpatterns = [
    path('', views.home_page, name='home')
]