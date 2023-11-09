from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Category, Product, Cart
# Create your views here.

def home(request):
	category_list = Category.objects.all()
	cart_list = Cart.objects.all()
	return render(request, 'main/home.html', context={
		'category_list':category_list,
		'cart_list': cart_list

	})



def cart(request):
	cart_list = Cart.objects.all()
	return render(request, 'main/cart.html', context={
		'cart_list': cart_list
	})


def prod(request, id):
	product_list = Category.objects.filter(pk=id)
	cart_list = Cart.objects.all()
	return render(request, 'main/prod.html', context={
		'product_list':product_list,
		'cart_list': cart_list
	})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")


def add_to_cart(request):
	if request.method == 'POST':
		prod_id = request.POST.get('prod_id')
		my_prod = Product.objects.get(id=prod_id)
		Cart.objects.create(product=my_prod)
		return redirect('home')
	

def delete_to_cart(request):
	if request.method == 'POST':
		prod_id = request.POST.get('prod_id')
		Cart.objects.get(pk=prod_id).delete()
		return redirect('cart')