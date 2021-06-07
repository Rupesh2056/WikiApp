from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry, name="entry"),
    path("add_entry/", views.add_entry, name="add-entry"),
    path("wiki/<str:title>/edit", views.edit_entry, name="edit-entry"),
    path("random/", views.random_entry, name="random-entry"),
]
