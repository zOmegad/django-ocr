from django.shortcuts import render
from favorite.models import SavedProduct

# Create your views here.

def my_save_food(request):
	my_food = SavedProduct.objects.filter(user=request.user)

	return render(request, 'my_save_food.html', {'my_food': my_food})
