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
    url('^duration/$', views.WidgetFormView.as_view(form_class=forms.DurationFieldForm), name="duration"),
    url('^email/$', views.WidgetFormView.as_view(form_class=forms.EmailFieldForm), name="email"),
    url('^file/$', views.WidgetFormView.as_view(form_class=forms.FileFieldForm), name="file"),
    url('^filepath/$',views.WidgetFormView.as_view(form_class=forms.FilePathFieldForm), name="filepath"),
    url('^float/$',views.WidgetFormView.as_view(form_class=forms.FloatFieldForm), name="float"),
    url('^image/$',views.WidgetFormView.as_view(form_class=forms.ImageFieldForm), name="image"),
    url('^integer/$',views.WidgetFormView.as_view(form_class=forms.IntegerFieldForm), name="integer"),
    url('^ipaddress/$',views.WidgetFormView.as_view(form_class=forms.GenericIPAddressFieldForm), name="ipaddress"),
    url('^multiplechoice/$',views.WidgetFormView.as_view(form_class=forms.MultipleChoiceFieldForm), name="multiplechoice"),
    url('^nullbolean/$',views.WidgetFormView.as_view(form_class=forms.NullBooleanFieldForm), name="nullbolean"),
    url('^regex/$',views.WidgetFormView.as_view(form_class=forms.RegexFieldForm), name="regex"),
    url('^slug/$',views.WidgetFormView.as_view(form_class=forms.SlugFieldForm), name="slug"),
    url('^time/$',views.WidgetFormView.as_view(form_class=forms.TimeFieldForm), name="time"),
    url('^url/$',views.WidgetFormView.as_view(form_class=forms.URLFieldForm), name="url"),
    url('^uuid/$',views.WidgetFormView.as_view(form_class=forms.UUIDField), name="uuid"),
    url('^combo/$',views.WidgetFormView.as_view(form_class=forms.ComboFieldForm), name="combo"),
    url('^splitdatetime/$',views.WidgetFormView.as_view(form_class=forms.SplitDateTimeFieldForm), name="splitdatetime"),
    url('^modelchoice/$',views.WidgetFormView.as_view(form_class=forms.ModelChoiceFieldForm), name="modelchoice"),
    url('^modelmultichoice/$',views.WidgetFormView.as_view(form_class=forms.ModelMultipleChoiceFieldForm), name="modelmultichoice"),

    url('^password/$', views.WidgetFormView.as_view(form_class=forms.PasswordInputForm), name="password"),
    url('^hidden/$', views.WidgetFormView.as_view(form_class=forms.HiddenInputForm), name="hidden"),
    url('^textarea/$', views.WidgetFormView.as_view(form_class=forms.TextareaForm), name="textarea"),
    url('^radioselect/$', views.WidgetFormView.as_view(form_class=forms.RadioSelectForm), name="radioselect"),
    # url('^checkboxmultiple/$', views.WidgetFormView.as_view(orm_class=forms.CheckboxSelectMultipleForm), name=""),
    url('^fileinput/$', views.WidgetFormView.as_view(form_class=forms.FileInputForm), name="fileinput"),
    url('^splithiddendatetime/$', views.WidgetFormView.as_view(form_class=forms.SplitHiddenDateTimeWidgetForm), name="splithiddendatetime"),
]

