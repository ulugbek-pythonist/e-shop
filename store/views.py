from django.shortcuts import get_object_or_404, render

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
    except Exception as e:
        print(f"{e}")

    contex = {
        "single_product": single_product,  # type: ignore
    }
    return render(request, "store/product_detail.html", context=contex)
