from django.contrib import admin
from .models import destination, scholarship
from .models import postinternship
from .models import events

# Register your models here.
admin.site.register(destination)
admin.site.register(postinternship)
admin.site.register(scholarship)
admin.site.register(events)