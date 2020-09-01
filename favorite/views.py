from django.shortcuts import render
from django.core.paginator import Paginator
from favorite.models import SavedProduct

# Create your views here.

def my_save_food(request):
	my_food = SavedProduct.objects.filter(user=request.user)
	paginator = Paginator(my_food, 6)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'my_save_food.html', {'my_food': my_food, 'page_obj': page_obj})
