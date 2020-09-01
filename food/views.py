from django.shortcuts import render, redirect
from food.models import *
from favorite.models import SavedProduct
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search(request):
	query = request.GET.get("query")
	if not query:
		pass
	else:
		product = Product.objects.filter(name__contains=query).first()
		category = Category.objects.get(pk=product.category_id)
		food_category = category.products.all()
		products = food_category.order_by('nutriscore',)

		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

	return render(request, 'food/products.html', {'products':page_obj, 'product': product, 'query': query})

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
