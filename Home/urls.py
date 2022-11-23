from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
    path("", views.index, name = "Home"),
    path("about", views.about, name = "About Us"),
    path("menu", views.menu, name = "Menu"),
    path("takeaway", views.takeaway, name = "Takeaway"),
    path("book", views.book, name = "book"),
    path("contact", views.contact, name = "Contact"),
]