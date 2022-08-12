from django.contrib import admin
from .models import Product, VolumeType, Comment

# Register your models here.
admin.site.register(Product)
admin.site.register(VolumeType)
admin.site.register(Comment)