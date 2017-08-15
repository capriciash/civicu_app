from django.http import HttpResponse

from django.shortcuts import render, redirect
from .models import Image
from .forms import FileUploadForm

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from . import models

def form_file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FileUploadForm()
    return render(request, 'labelgame/form_file_upload.html', {
        'form': form
    })

def index(request):
    images = Image.objects.all()
    return render(request, 'labelgame/index.html', {'images': images})

# def index(request):
#     return HttpResponse("Hello, world. You're in the Animal Labeler App.")

class ListImages(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer
