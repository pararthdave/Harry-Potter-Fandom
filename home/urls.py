from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='Home'),
    path("about", views.about, name='About'),
    path("books", views.books, name='Books'),
    path("contact", views.contact, name='Contact'),
    path("ff", views.ff, name="FF"),
    path("pb1", views.pb1, name='Pb1'),
    path("pb2", views.pb2, name='Pb2'),
    path("pb3", views.pb3, name='Pb3'),
    path("pb4", views.pb4, name='Pb4'),
    path("pb5", views.pb5, name='Pb5'),
    path("pb6", views.pb6, name='Pb6'),
    path("pb7", views.pb7, name='Pb7'),
]


