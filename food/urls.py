from django.conf.urls import url, include

from . import views


urlpatterns = [
	url(r'products/', views.products),
    url(r'^better/(?P<food_id>\d+)/$', views.better, name='better'),
    url(r'^better/(?P<food_id>\d+)/save_product', views.save_product, name='save_product'),
    url(r'^$', views.index),
	url(r'food/', views.index),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
]
