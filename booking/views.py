from datetime import datetime

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404 ,render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Room, TimeSlot, Meeting, Username

# Create your views here.
def index(request):
    return render(request, 'booking/index.html')


def dashboard(request, username):
    """
    This page will serve as user's dashboard - showing how many meeting
    users will have for the time period they choose (default = today).
    There will be entry to start booking meeting rooms from this page as well
    """
    username_id = Username.objects.get(username=username).id
    meeting_list = Meeting.objects.filter(username_id=username_id,
                                        meeting_date=datetime.today())
    return render(request, 'booking/dashboard.html', {
        'meeting_list': meeting_list,
        'username': username})


def create_meeting(request, username):
    """
    This page will be the booking flow. Nots sure whether I should put This
    as part of user dashboard or start a new page.
    """
    return render(request, 'booking/create_meeting.html', {'username': username})
