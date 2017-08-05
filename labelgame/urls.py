from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^upload/$', views.form_file_upload, name='form_file_upload'),
    url(r'^$', views.index, name='index'),
]
