from django.shortcuts import render, redirect
from food.models import *

def index(request):
	query = request.POST.get("query")
	if not query:
		pass
	else:
		products = Product.objects.filter(name__contains=query)
		return render(request, 'food/products.html', {'products':products})

	return render(request, 'food/index.html')

def products(request):
	products = Product.objects.all()
	categories = Category.objects.all()
	query = request.POST.get("query")
	return render(request, 'food/products.html', {'products':products, 'categories':categories})

def better(request, food_id):
	food = Product.objects.get(pk=food_id)
	category = Category.objects.get(pk=food.category_id)
	food_category = category.products.all()
	better_food = food
	for item in food_category:
		if better_food.nutriscore > item.nutriscore:
			better_food = item
		else:
			pass

	return render(request, 'food/better.html', {'product': food, 'new_product': better_food})

def save_product(request, food_id):
	print('lol')
	food = Product.objects.get(pk=food_id)
	new_save = SavedProduct(product_id=food_id, user=request.user)
	new_save.save()
	return redirect('/')
