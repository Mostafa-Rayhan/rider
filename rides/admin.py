from django.contrib import admin
from .models import User
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Riders)
admin.site.register(Measurement)
