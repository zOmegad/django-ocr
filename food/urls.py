from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.index,
        name='index'),
    path(
        '<int:food_id>/',
        views.show,
        name='show'),
    path(
        '<int:food_id>/save_product',
        views.save_product,
        name='save_product'),
]
