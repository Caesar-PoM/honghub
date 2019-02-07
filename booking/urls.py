from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('<str:username>/dashboard', views.dashboard, name='dashboard'),
    path('<str:username>/booking', views.booking, name='booking'),
]
