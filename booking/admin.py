from django.contrib import admin

from .models import Building, Room, TimeSlot, Username, Meeting

# Register your models here.
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(TimeSlot)
admin.site.register(Username)
admin.site.register(Meeting)
