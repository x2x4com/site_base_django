from django.conf.urls import url, include
from django.views import generic

from . import views


urlpatterns = [
    url('^$', generic.RedirectView.as_view(url='./index/'), name="index"),
    url('^index/', views.index, name="default"),
    url('^data.json', views.data, name="data"),
    url('^fc/', views.form_create, name="fc"),
]