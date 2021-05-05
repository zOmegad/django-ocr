from django.urls import path

from . import views


urlpatterns = [
    path('mentionslegales', views.mentions, name="mentions"),
]
