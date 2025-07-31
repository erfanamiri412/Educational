from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm

def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

def about(request):
    return render(request, 'shop/about.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید')
            return redirect('index')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
    return render(request, 'shop/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'شما با موفقیت خارج شدید')
    return redirect('index')

def signup_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'شما با موفقیت ثبت نام کردید')
                return redirect('index')
        messages.error(request, 'ثبت نام شما موفقیت‌آمیز نبود')
    return render(request, 'shop/signup.html', {'form': form})

def category(request, cat):
    cat = cat.replace("-", " ")
    try:
        category_obj = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category_obj)
        return render(request, 'shop/category.html', {'products': products, 'category': category_obj})
    except Category.DoesNotExist:
        messages.error(request, 'دسته بندی وجود ندارد')
        return redirect('index')

def product(request, pk):
    try:
        product_obj = Product.objects.get(pk=pk)
        return render(request, 'shop/product.html', {'product': product_obj})
    except Product.DoesNotExist:
        messages.error(request, 'محصول مورد نظر پیدا نشد')
        return redirect('index')