
from django.utils.translation import ugettext_lazy as _

from material import Layout, Row, Fieldset
from material.frontend.views import ModelViewSet

from django.shortcuts import render
from django.views import generic, static
from django.contrib.auth.decorators import login_required
from formtools.wizard.views import SessionWizardView

from . import models
from . import forms

# class MyModelViewSet(ModelViewSet):
#    model = models.MyModel


class WidgetFormView(generic.FormView):
    template_name = 'material/frontend/base_forms.html'

    # require login
    @classmethod
    def as_view(cls, *args, **kwargs):
        return login_required(super(WidgetFormView, cls).as_view(*args, **kwargs))

    def form_valid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form))


class Wizard(SessionWizardView):
    form_list = [forms.WizardForm1, forms.WizardForm2]

    def done(self, form_list, **kwargs):
        return render(self.request, 'formtools/wizard/wizard_done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
