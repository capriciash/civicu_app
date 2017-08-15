from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^api/v1/images/$', views.ListImages.as_view(), name='list_image_api'),
    url(r'^upload/$', views.form_file_upload, name='form_file_upload'),
    url(r'^$', views.index, name='index'),
]
