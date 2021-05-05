from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from favorite.models import SavedProduct


def my_save_food(request):
    if request.user.is_authenticated:
        my_food = SavedProduct.objects.filter(user=request.user).order_by('id')
        paginator = Paginator(my_food, 6)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request, 'my_save_food.html', {
                'my_food': my_food, 'page_obj': page_obj})
    else:
        return redirect('/')
