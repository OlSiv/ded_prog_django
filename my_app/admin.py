from django.contrib import admin
from my_app.models import Worker    ### new

# Register your models here.
admin.site.register(Worker)   ### new
