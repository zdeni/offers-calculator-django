from django.urls import path
from . import views

urlpatterns = [
    # Products
    path("products/", views.product_list, name="product_list"),
    path("products/new/", views.product_create, name="product_create"),

    # Services
    path("services/", views.service_list, name="service_list"),
    path("services/new/", views.service_create, name="service_create"),

    # Raw materials
    path("materials/", views.material_list, name="material_list"),
    path("materials/new/", views.material_create, name="material_create"),
]
