from django.shortcuts import get_object_or_404, render
from carts.models import CartItem
from carts.views import _cart_id

from category.models import Category
from .models import Product


def store(request, categor_slug=None):
    categories = None
    products = None

    if categor_slug != None:
        categories = get_object_or_404(Category, slug=categor_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    contextim = {"products": products, "counter": product_count}
    return render(request, "store/store.html", context=contextim)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug
        )
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), product=single_product
        ).exists()

    except Exception as e:
        raise e

    contex = {
        "single_product": single_product,  # type: ignore
        "in_cart": in_cart,  # type: ignore
    }
    return render(request, "store/product_detail.html", context=contex)
