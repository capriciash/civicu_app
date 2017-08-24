
""" Profile model with first and last name, an image, and profile description
    Label model with image ID and chosen classification
    Image model with image ID and path to the image on a shared server or a binary blob of the image itself
"""
# import datetime

from django.db import models
from django.contrib import admin
# from django.utils import timezone
from django.contrib.auth.models import User

Wolf = 'Wolf'
Bear = 'Bear'
Monkey = 'Monkey'
NotAnimal = 'Not an Animal'
Skipped = 'Skipped'
Animal_Choices = (
    (Wolf, 'Wolf'),
    (Bear, 'Bear'),
    (Monkey, 'Monkey'),
    (NotAnimal, 'NotAnimal'),
    (Skipped, 'Skipped'),
)

class Image(models.Model):
    """ A database record for uploaded images to be labeled """
    caption = models.CharField("Description of the image, where and when it was taken",
                               max_length=512, default=None, null=True)
    uploaded_by = models.ForeignKey(User, default=None, null=True)
    img_file = models.FileField("Select file to upload", upload_to='images')
    date_taken = models.DateField('Date photo was taken.',blank=True, null=True)
    updated_date = models.DateTimeField('Date photo was changed.', auto_now=True)
    created_date = models.DateTimeField('Date photo was uploaded.', auto_now_add=True)
    def __str__(self):
        return self.caption

class Admin_Image(admin.ModelAdmin):
    date_hierarchy = 'date_taken'
    list_display = ('caption', 'img_file', 'date_taken', 'created_date', 'uploaded_by')

class UserLabel(models.Model):
    """ Individual user labels (their filled out ballot, voting for a label for an image) """
    # name = models.CharField(max_length=128)
    user = models.ForeignKey(User, default=None, null=True)
    sel_animal = models.CharField(max_length=20, choices=Animal_Choices, default=None, null=True)
    sel_date = models.DateTimeField('date selected',auto_now_add=True)
    image = models.ForeignKey(Image, default=None, null=True)
    # def __str__(self):
    #     return self.name
    # def was_voted_recently(self):
    #     return self.sel_date >= timezone.now() - datetime.timedelta(days=1)

class Admin_Label(admin.ModelAdmin):
    list_display = ('image', 'user', 'sel_animal', 'sel_date')
    list_filter = ('image', 'user')

class TotalVotes(models.Model):
    """ Aggregated votes (by all users, who are allowed to vote multiple times) for an individual Image """
    image = models.ForeignKey(Image, default=None, null=True)
    name = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "total votes"
