from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from carts.models import CartItem
from carts.views import _cart_id

from category.models import Category
from .models import Product


def store(request, categor_slug=None):
    categories = None
    products = None

    if categor_slug != None:
        categories = get_object_or_404(Category, slug=categor_slug)
        products = Product.objects.filter(
            category=categories, is_available=True
        ).order_by("id")
        paginator = Paginator(products, 1)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by("id")
        paginator = Paginator(products, 3)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
        product_count = products.count()
    contextim = {"products": paged_products, "counter": product_count}
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


def search(request):
    if "keyword" in request.GET:
        keyword = request.GET["keyword"]

    if keyword:
        products = Product.objects.all().filter(
            Q(description__icontains=keyword) | Q(title__icontains=keyword)
        )
        product_count = products.count()

    cont = {
        "products": products,
        "product_count": product_count,
    }

    return render(request, "store/store.html", context=cont)
