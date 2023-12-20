from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.


def category(request,bag):
    # Replace Hyphens with Spaces
    bag = bag.replace('-',' ')
    # Grab the category from the url
    try:
        # Look up Category
        category = Category.objects.get(name=bag)
        products = Product.objects.filter(category=category)
        return render(request,'category.html', {'products':products, 'category':category})

    except:
        messages.success(request,("Sorry, No Such Category."))
        return redirect('home')

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

def home(request):
    products = Product.objects.all
    return render(request,'home.html',{'products':products})

def about(request):
    return render(request,'about.html')


def register_user(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            #log in user
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("Registration successful. Welcome!."))
            return redirect('home')
        else:
            messages.success(request,("Error... Please fill all required fields."))
            return redirect('register')
    else:


       return render(request,'register.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username=username,password=password)

       if user is not None:
           login(request, user)
           messages.success(request,("You Have Been Logged In Successfully!."))
           return redirect('home')
       else:
           messages.success(request,("Wrong details. Please Enter a Correct Username and  Password."))
           return redirect('login')
           
    else:

     return render(request,'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request,("You Have Been Logged Out Successfully."))
    return redirect ('home')
