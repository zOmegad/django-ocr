from django.shortcuts import render, redirect
from food.models import *
from favorite.models import SavedProduct


def index(request):
	return render(request, 'food/index.html')

def show(request, food_id):
	food = Product.objects.get(pk=food_id)
	return render(request, 'food/show.html', {'product': food})

def save_product(request, food_id):
	food = Product.objects.get(pk=food_id)
	new_save = SavedProduct(product_id=food_id, user=request.user)
	new_save.save()
	return redirect('/')
