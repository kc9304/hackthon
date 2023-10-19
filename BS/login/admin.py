from django.contrib import admin

from .models import Comic, Personal

# Register your models here.
admin.site.register(Comic)
admin.site.register(Personal)