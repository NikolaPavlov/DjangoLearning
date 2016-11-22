from django.shortcuts import render
from .models import Category, Product


# Create your views here.
def index(request):
    all_categories = Category.objects.all()
    context = {'categories': all_categories}
    return render(request, 'store/index.html', context)


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'store/detail.html', context)
