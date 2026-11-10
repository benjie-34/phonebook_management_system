from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact_list, name="contact_list"),
    path("contacts/add/", views.contact_create, name="contact_create"),
    path("contacts/<int:pk>/", views.contact_detail, name="contact_detail"),
    path("contacts/<int:pk>/edit/", views.contact_update, name="contact_update"),
    path("contacts/<int:pk>/delete/", views.contact_delete, name="contact_delete"),
]
