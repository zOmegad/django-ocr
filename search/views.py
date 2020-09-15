from django.shortcuts import render, redirect
from django.urls import reverse
from food.models import Product, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def search(request):
	query = request.GET.get("query")
	if not query:
		pass
	else:
		product = Product.objects.filter(name__contains=query).first()
		if not product:
			return render(request, 'search.html', {'nil_query': query})
		else:
			category = Category.objects.get(pk=product.category_id)
			food_category = category.products.all()
			products = food_category.order_by('nutriscore',)

			paginator = Paginator(products, 12)
			page_number = request.GET.get('page')
			page_obj = paginator.get_page(page_number)

	return render(request, 'search.html', {'products':page_obj, 'product': product, 'query': query})

def not_found(request):
	return render(request, 'not_found.html')
