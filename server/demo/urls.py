from django.conf.urls import url, include
from django.views import generic

from . import views
from . import forms

urlpatterns = [
    url('^$', generic.RedirectView.as_view(url='./wizard/'), name="index"),
    url('^wizard/$', views.Wizard.as_view(), name="wizard"),
    url('^selectdate/$', views.WidgetFormView.as_view(form_class=forms.SelectDateWidgetForm), name="selectdate"),
    url('^char/$', views.WidgetFormView.as_view(form_class=forms.CharFieldForm), name="char"),
    url('^choice/$', views.WidgetFormView.as_view(form_class=forms.ChoiceFieldForm), name="choice"),
    url('^date/$', views.WidgetFormView.as_view(form_class=forms.DateFieldForm), name="date"),
    url('^datetime/$', views.WidgetFormView.as_view(form_class=forms.DateTimeFieldForm), name="datetime"),
    url('^decimal/$', views.WidgetFormView.as_view(form_class=forms.DecimalFieldForm), name="decimal"),
    url('^duration/$', views.WidgetFormView.as_view(form_class=forms.DurationFieldForm)),
    url('^email/$', views.WidgetFormView.as_view(form_class=forms.EmailFieldForm)),
    url('^file/$', views.WidgetFormView.as_view(form_class=forms.FileFieldForm)),
    url('^filepath/$',views.WidgetFormView.as_view(form_class=forms.FilePathFieldForm)),
    url('^float/$',views.WidgetFormView.as_view(form_class=forms.FloatFieldForm)),
    url('^image/$',views.WidgetFormView.as_view(form_class=forms.ImageFieldForm)),
    url('^integer/$',views.WidgetFormView.as_view(form_class=forms.IntegerFieldForm)),
    url('^ipaddress/$',views.WidgetFormView.as_view(form_class=forms.GenericIPAddressFieldForm)),
    url('^multiplechoice/$',views.WidgetFormView.as_view(form_class=forms.MultipleChoiceFieldForm)),
    url('^nullbolean/$',views.WidgetFormView.as_view(form_class=forms.NullBooleanFieldForm)),
    url('^regex/$',views.WidgetFormView.as_view(form_class=forms.RegexFieldForm)),
    url('^slug/$',views.WidgetFormView.as_view(form_class=forms.SlugFieldForm)),
    url('^time/$',views.WidgetFormView.as_view(form_class=forms.TimeFieldForm)),
    url('^url/$',views.WidgetFormView.as_view(form_class=forms.URLFieldForm)),
    url('^uuid/$',views.WidgetFormView.as_view(form_class=forms.UUIDField)),
    url('^combo/$',views.WidgetFormView.as_view(form_class=forms.ComboFieldForm)),
    url('^splitdatetime/$',views.WidgetFormView.as_view(form_class=forms.SplitDateTimeFieldForm)),
    url('^modelchoice/$',views.WidgetFormView.as_view(form_class=forms.ModelChoiceFieldForm)),
    url('^modelmultichoice/$',views.WidgetFormView.as_view(form_class=forms.ModelMultipleChoiceFieldForm)),

    url('^password/$', views.WidgetFormView.as_view(form_class=forms.PasswordInputForm)),
    url('^hidden/$', views.WidgetFormView.as_view(form_class=forms.HiddenInputForm)),
    url('^textarea/$', views.WidgetFormView.as_view(form_class=forms.TextareaForm)),
    url('^radioselect/$', views.WidgetFormView.as_view(form_class=forms.RadioSelectForm)),
    # url('^checkboxmultiple/$', views.WidgetFormView.as_view(orm_class=forms.CheckboxSelectMultipleForm)),
    url('^fileinput/$', views.WidgetFormView.as_view(form_class=forms.FileInputForm)),
    url('^splithiddendatetime/$', views.WidgetFormView.as_view(form_class=forms.SplitHiddenDateTimeWidgetForm)),
]

