from django.shortcuts import get_object_or_404 ,render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Room, TimeSlot

# Create your views here.
def index(request):
    return render(request, 'booking/index.html')


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


def create_meeting(request, username):
    """
    This page will be the booking flow. Nots sure whether I should put This
    as part of user dashboard or start a new page.
    """
    return render(request, 'booking/create_meeting.html', {'username': username})
