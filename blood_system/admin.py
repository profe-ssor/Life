from django.contrib import admin

from .models import Register_as_Donor
from .models import Request_for_blood
from .models import Message
from .models import    Room
from .models import Topic

admin.site.register(Register_as_Donor)
admin.site.register(Request_for_blood)
admin.site.register(Message)
admin.site.register(Room)
admin.site.register(Topic)
