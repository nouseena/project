from django.urls import path
from .import views

urlpatterns= [
    path('',views.fn_index),
    path('login/',views.fn_login)
]