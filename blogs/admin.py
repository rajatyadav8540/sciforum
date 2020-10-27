from django.contrib import admin
from .models import blogpost,blogComment

# Register your models here.
admin.site.register((blogpost,blogComment))