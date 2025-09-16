from django.shortcuts import get_object_or_404, render

from shop_app.models import Category, Product

# Create your views here.
def index(request):
    categories = Category.objects.all()  # Admin-д байгаа бүх category
    popular_products = Product.objects.all()[:9]  # Жишээ: хамгийн эхний 8 product
    context = {
        'categories': categories,
        'popular_products': popular_products
    }
    return render(request, 'index.html', context)
def cart(request):
    return render(request , "cart.html")
def dashboard(request):
    return render(request , "dashboard.html")
def order_complete(request):
    return render(request , "order-complete.html")
def place_order(request):
    return render(request , "place-order.html")
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})

def register(request):
    return render(request , "register.html")
def search_result(request):
    return render(request , "search-result.html")
def signin(request):
    return render(request , "signin.html")
def store(request):
    return render(request , "store.html")

def category_products(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {'category': category, 'products': products})




