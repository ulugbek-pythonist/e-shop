from django.urls import path

from .views import add_cart, cart, remove_cart, remove_cart_item

urlpatterns = [
    path("", cart, name="cart"),
    path("add_cart/<int:product_id>/", add_cart, name="add_cart"),
    path("rem_cart/<int:product_id>/", remove_cart, name="rem_cart"),
    path("rem_cartitem/<int:product_id>/", remove_cart_item, name="rem_cartitem"),
]
