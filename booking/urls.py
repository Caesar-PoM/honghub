from django.urls import path

from . import views

app_name = 'booking'
urlpatterns = [
	path('', views.index, name='index'),
    path('<str:username>/', views.dashboard, name='dashboard'),
    path('<str:username>/create_meeting', views.create_meeting, name='create_meeting'),
]
