from django.conf.urls import url, include
from django.views import generic

from . import views
from . import forms

urlpatterns = [
    url('^$', generic.RedirectView.as_view(url='./wizard/'), name="index"),
    url('^selectdate/$', views.WidgetFormView.as_view(form_class=forms.SelectDateWidgetForm), name="selectdate"),
    url('^wizard/$', views.Wizard.as_view(), name="wizard"),
]

