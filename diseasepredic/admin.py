from django.contrib import admin
from .models import Symptoms,Diseases,combination

admin.site.register(Symptoms)
admin.site.register(Diseases)
admin.site.register(combination)
