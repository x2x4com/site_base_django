from django.conf.urls import url, include
from django.views import generic

from . import views

urlpatterns = [
    url('^$', generic.RedirectView.as_view(url='./control/'), name="index"),
    url('^control/', include(views.SomeControlViewSet().urls)),
    url('^type/', include(views.SomeControlTypeViewSet().urls)),
    url(r'^tags/', include(views.SomeControlTagsViewSet().urls)),
]

