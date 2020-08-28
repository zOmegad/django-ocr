from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'my_save_food/', views.my_save_food),
]
