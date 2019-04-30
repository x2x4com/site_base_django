from django.conf.urls import url, include
from django.views import generic

from . import views

urlpatterns = [
    url('^$', generic.RedirectView.as_view(url='./list/'), name="index"),
    url('^list/', include(views.NewsViewSet().urls)),
    url('^type/', include(views.TypeViewSet().urls)),
]
