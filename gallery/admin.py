from django.contrib import admin
from .models import Image, Comments, Deleted_Comments
# Register your models here.


admin.site.register(Image)
admin.site.register(Comments)
admin.site.register(Deleted_Comments)