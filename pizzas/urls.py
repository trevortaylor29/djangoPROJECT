from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("pizzas/", views.pizzas, name="pizzas"),
    path("pizzas/<int:pizza_id>/", views.pizza, name="pizza"),
    path("pizzas/<int:pizza_id>/comment/", views.comment_form, name="comment_form"),
]



