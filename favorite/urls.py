from django.urls import path

from . import views


urlpatterns = [
    path('my_save_food/', views.my_save_food, name="saved_food"),
]
