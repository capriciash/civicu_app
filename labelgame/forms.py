from django import forms
from .models import Image

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('img_file', 'caption', 'uploaded_by')
