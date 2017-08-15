from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.ListCreateMovies.as_view(), name='movies_list'),
]
