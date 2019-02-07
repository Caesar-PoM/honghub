from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Room, TimeSlot

# Create your views here.
def index(request):
    """
    This page will be used as landing page. This page should have
    register and login button for new existing users respectively
    """
    return HttpResponse('Index')


def dashboard(request, username):
    """
    This page will serve as user's dashboard - showing how many meeting
    users will have for the time period they choose (default = weekly).
    There will be entry to start booking meeting rooms from this page as well
    """
    time_slot_list = TimeSlot.objects.all()
    return render(request, 'booking/dashboard.html', {
        'time_slot_list': time_slot_list,
        'username': username})


def booking(request):
    """
    This page will be the booking flow. Nots sure whether I should put This
    as part of user dashboard or start a new page.
    """
    return HttpResponse('booking flow')
