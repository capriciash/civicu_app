from django.contrib import admin

from .models import Image, UserLabel, TotalVotes, Admin_Image, Admin_Label

# Register your models here.
admin.site.register(Image, Admin_Image)
admin.site.register(UserLabel, Admin_Label)
admin.site.register(TotalVotes)
