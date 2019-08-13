from django.urls import path
from .views import APILojaView

urlpatterns = [
    path('lojas/', APILojaView.as_view())
]