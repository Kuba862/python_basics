from django.contrib import admin
from .models import Petition, Topics

admin.site.register(Petition)
admin.site.register(Topics)