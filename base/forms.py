#!/usr/bin/env python
# encoding: utf-8
# ===============================================================================
#
#         FILE:
#
#        USAGE:
#
#  DESCRIPTION:
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:  YOUR NAME (),
#      COMPANY:
#      VERSION:  1.0
#      CREATED:
#     REVISION:  ---
# ===============================================================================

from django.template import Template
from . import _forms as forms
from material import Layout, Row, Column, Fieldset, Span2, Span3, Span5, Span6, Span10
from ._choose import *


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    keep_logged = forms.BooleanField(required=False, label="Keep me logged in")

    template = Template("""
    {% form %}
        {% part form.email prefix %}<i class="material-icons prefix">email</i>{% endpart %}
        {% part form.password prefix %}<i class="material-icons prefix">lock</i>{% endpart %}
        {% attr form.keep_logged 'group' class append %}right-align{% endattr %}
    {% endform %}
    """)

    buttons = Template("""
        <button class="waves-effect waves-teal btn-flat">Register</button>
        <button class="waves-effect waves-light btn" type="submit">Login</button>
    """)

    title = "Login form"

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if cleaned_data.get('email') == 'john@doe.com':
            raise forms.ValidationError('John, come on. You are blocked.')


class RegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    gender = forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')))
    receive_news = forms.BooleanField(required=False, label='I want to receive news and special offers')
    agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')

    layout = Layout('username', 'email',
                    Row('password', 'password_confirm'),
                    Fieldset('Personal details',
                             Row('first_name', 'last_name'),
                             'gender', 'receive_news', 'agree_toc'))

    template = Template("""
    {% form %}
        {% part form.username prefix %}<i class="material-icons prefix">account_box</i>{% endpart %}
        {% part form.email prefix %}<i class="material-icons prefix">email</i>{% endpart %}
        {% part form.password prefix %}<i class="material-icons prefix">lock_open</i>{% endpart %}
    {% endform %}
    """)

    buttons = Template("""
        <button class="waves-effect waves-light btn" type="submit">Submit</button>
    """)

    title = "Registration form"


class CheckoutForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    country = forms.ChoiceField(choices=COUNTRY_CHOICES)
    city = forms.CharField()
    post_code = forms.IntegerField()
    address = forms.CharField()
    additional_info = forms.CharField(widget=forms.Textarea)
    card_type = forms.ChoiceField(choices=(('V', 'Visa'), ('M', 'MasterCard'), ('P', 'Paypal')), widget=forms.RadioSelect)
    card_holder = forms.CharField(label="Name on card")
    card_number = forms.CharField(label="Card number")
    card_ccv2 = forms.IntegerField(label="CVV2")
    card_exp_month = forms.ChoiceField(choices=((1, 'January'), (2, 'February'), (3, 'March'),
                                                (4, 'April'), (5, 'May'), (6, 'June'),
                                                (7, 'July'), (8, 'August'), (9, 'September'),
                                                (10, 'October'), (11, 'November'), (12, 'December')))
    card_exp_year = forms.IntegerField(label="Year")

    layout = Layout(
        Row('first_name', 'last_name'),
        Row('email', 'phone'),
        Row(Span5('country'), Span5('city'), Span2('post_code')),
        'address',
        'additional_info',
        Fieldset('Card Details',
                 Row(Column('card_type', span_columns=4),
                     Column('card_holder',
                            Row(Span10('card_number'), Span2('card_ccv2')),
                            Row('card_exp_month', 'card_exp_year'),
                            span_columns=8))))

    template = Template("""
    {% form %}
        {% part form.first_name prefix %}<i class="material-icons prefix">account_box</i>{% endpart %}
        {% part form.last_name prefix %}<i class="material-icons prefix">account_box</i>{% endpart %}
        {% part form.email prefix %}<i class="material-icons prefix">email</i>{% endpart %}
        {% part form.phone prefix %}<i class="material-icons prefix">call</i>{% endpart %}
        {% part form.card_type label %}{% endpart %}
    {% endform %}
    """)

    buttons = Template("""
        <button class="btn btn-primary pull-right" type="submit">Submit request</button>
    """)

    title = "Checkout form"

    css = """
    @media only screen and (min-width : 601px) {
        #id_card_type_container {
            margin-top: 40px;
            margin-left: 50px;
      }
    """


class OrderForm(forms.Form):
    name = forms.CharField()
    company = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    interest = forms.ChoiceField(choices=((None, 'Interested in'), ('D', 'Design'), ('C', 'Development'),
                                          ('I', 'Illustration'), ('B', 'Branding'), ('V', 'Video')))
    budget = forms.ChoiceField(choices=((None, 'Budget'), ('S', 'Less than $5000'), ('M', '$5000-$10000'),
                                        ('L', '$10000-$20000'), ('XL', 'More than $20000')))
    start_date = forms.DateField(label="Expected start date")
    finish_date = forms.DateField(label="Expected finish date")
    attachment = forms.FileField(label="Include some file...")
    message = forms.CharField(widget=forms.Textarea)

    layout = Layout('name', 'company', 'email', 'phone',
                    Row('interest', 'budget'),
                    Row('start_date', 'finish_date'),
                    'attachment', 'message')

    template = Template("""
    {% form %}
        {% part form.name prefix %}<i class="material-icons prefix">account_box</i>{% endpart %}
        {% part form.company prefix %}<i class="material-icons prefix">business</i>{% endpart %}
        {% part form.email prefix %}<i class="material-icons prefix">email</i>{% endpart %}
        {% part form.phone prefix %}<i class="material-icons prefix">call</i>{% endpart %}
    {% endform %}
    """)

    buttons = Template("""
        <button class="btn btn-primary pull-right" type="submit">Submit request</button>
    """)

    title = "Order services"


class CommentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
    layout = Layout(Row('name', 'email'),
                    'website', 'comment')

    template = Template("""
    {% form %}
        {% part form.name prefix %}<i class="material-icons prefix">account_box</i>{% endpart %}
        {% part form.email prefix %}<i class="material-icons prefix">email</i>{% endpart %}
        {% part form.website prefix %}<i class="material-icons prefix">card_travel</i>{% endpart %}
        {% part form.comment prefix %}<i class="material-icons prefix">chat</i>{% endpart %}
    {% endform %}
    """)

    buttons = Template("""
        <button class="btn btn-primary pull-right" type="submit">Add comment</button>
    """)

    title = "Comment form"


class BankForm(forms.Form):
    branch_name = forms.CharField()

    """ Personal Details """
    person_title = forms.ChoiceField(choices=(('Mr', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')), label='Title')
    full_name = forms.CharField()
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    parent_name = forms.CharField(label='In case of a minor please provide details')
    nationality = forms.ChoiceField(choices=COUNTRY_CHOICES)
    mobile_no = forms.CharField()
    existing_bank_account = forms.CharField()
    partner_name = forms.CharField(label='Name of father/spouse')

    """ Residential address """
    flat_bulding = forms.CharField(label='Flat no. and bldg. name')
    road_no = forms.CharField(label='Road no./name')
    area_and_landmark = forms.CharField(label='Area and landmark')
    telephone_residence = forms.CharField()
    city = forms.CharField()
    office = forms.CharField()
    fax = forms.CharField()
    pin_code = forms.CharField()

    """ Mailing Address """
    mailing_company_details = forms.CharField(label="Company name and department/ Flat no. and bldg. name")
    mailing_road_no = forms.CharField(label='Road no./name')
    mailing_area_and_landmark = forms.CharField(label='Area and landmark')
    mailing_city = forms.CharField(label='City')
    mailing_mobile = forms.CharField(label='Mobile No.')
    mailing_telephone_residence = forms.CharField(label='Telephone Residence')
    mailing_office = forms.CharField(label='Office')
    mailing_fax = forms.CharField(label='Fax')
    mailing_pin_code = forms.CharField(label='Pin Code')
    mailing_email = forms.EmailField(label='E-mail')

    """ Details of Introduction by Existing Customer """
    introducer_name = forms.CharField(label='Customer Name')
    introducer_account_no = forms.CharField(label='Account No.')
    introducer_signature = forms.CharField(label="Introducer's signature")

    """ Account Details """
    account_type = forms.ChoiceField(
        choices=(('S', 'Savings'), ('C', 'Current'), ('F', 'Fixed deposits')),
        label='Choice of account',
        widget=forms.RadioSelect)
    account_mode = forms.ChoiceField(
        choices=(('CS', 'Cash'), ('CQ', 'Cheque'), ('NF', 'NEFT')),
        label='Mode of funding',
        widget=forms.RadioSelect)
    account_amount = forms.FloatField(label='Amount')

    """ Details of Fixed Deposit """
    deposit_type = forms.ChoiceField(
        choices=(('O', 'Ordinary'), ('C', 'Cumulative')),
        label='Types of deposit',
        widget=forms.RadioSelect)
    deposit_mode = forms.ChoiceField(
        choices=(('CS', 'Cash'), ('CQ', 'Cheque'), ('NF', 'NEFT')),
        label='Mode of funding',
        widget=forms.RadioSelect)
    deposit_amount = forms.FloatField(label='Amount')
    deposit_no = forms.CharField(label='No. of deposits')
    deposit_individual_amount = forms.FloatField(label='Individual Deposit Amount')

    """ Personal Details """
    occupation = forms.ChoiceField(
        choices=(('NE', 'Non-executive'), ('HW', 'Housewife'), ('RT', 'Retired'),
                 ('ST', 'Student'), ('OT', 'Other'), ('UN', 'Unemployed')),
        widget=forms.RadioSelect)
    job_title = forms.CharField()
    department = forms.CharField()
    nature_of_business = forms.CharField()
    education = forms.ChoiceField(
        choices=(('UG', 'Under graduate'), ('GR', 'Graduate'), ('OT', 'Others')),
        widget=forms.RadioSelect)
    montly_income = forms.ChoiceField(
        choices=(('000', 'Zero Income'), ('L10', 'Less than $10,000'), ('G10', '$10,000+')),
        widget=forms.RadioSelect)
    martial_status = forms.ChoiceField(
        choices=(('M', 'Married'), ('S', 'Single')),
        widget=forms.RadioSelect)
    spouse_name = forms.CharField()

    """ Other existing bank accounts, if any """
    other_account1 = forms.CharField(label='Name of the Bank / branch')
    other_account2 = forms.CharField(label='Name of the Bank / branch')

    """ Reason for Account opening """
    reason = forms.CharField(label="Please specify", widget=forms.Textarea)

    """ Terms And Conditions """
    terms_accepted = forms.BooleanField(
        label="I/We confirm having read and understood the account rules of The Banking Corporation Limited"
        " ('the Bank'), and hereby agree to be bound by the terms and conditions and amendments governing the"
        " account(s) issued by the Bank from time-to-time.")

    layout = Layout(
        Fieldset("Please open an account at",
                 'branch_name'),
        Fieldset("Personal Details (Sole/First Accountholder/Minor)",
                 Row(Span2('person_title'), Span10('full_name')),
                 Row(Column('date_of_birth',
                            'email',
                            'parent_name'),
                     Column('nationality',
                            Row('mobile_no', 'existing_bank_account'),
                            'partner_name'))),
        Fieldset('Residential address',
                 Row('flat_bulding', 'road_no'),
                 Row(Span10('area_and_landmark'), Span2('city')),
                 Row('telephone_residence', 'office', 'fax', 'pin_code')),
        Fieldset("Mailing Address (If different from the First Accountholder's address)",
                 'mailing_company_details',
                 Row('mailing_road_no', 'mailing_area_and_landmark', 'mailing_city', 'mailing_mobile'),
                 Row('mailing_telephone_residence', 'mailing_office', 'mailing_fax', 'mailing_pin_code'),
                 'mailing_email'),
        Fieldset("Details of Introduction by Existing Customer (If applicable)",
                 Row('introducer_name', 'introducer_account_no'),
                 'introducer_signature'),
        Fieldset("Account Details",
                 Row('account_type', 'account_mode'),
                 'account_amount'),
        Fieldset("Details of Fixed Deposit",
                 Row('deposit_type', 'deposit_mode'),
                 Row(Span6('deposit_amount'), Span3('deposit_no'), Span3('deposit_individual_amount'))),
        Fieldset("Personal Details",
                 Row('occupation', 'education', 'montly_income'),
                 'job_title',
                 Row('department', 'nature_of_business'),
                 Row('martial_status', 'spouse_name')),
        Fieldset("Other existing bank accounts, if any",
                 Row('other_account1', 'other_account2')),
        Fieldset("Reason for Account opening",
                 'reason'),
        Fieldset("Terms And Conditions",
                 'terms_accepted')
    )

    template = Template("""
    {% form %}
        {% attr form.account_type 'group' class append %}inline{% endattr %}
        {% attr form.account_mode 'group' class append %}inline{% endattr %}
        {% attr form.deposit_type 'group' class append %}inline{% endattr %}
        {% attr form.deposit_mode 'group' class append %}inline{% endattr %}
        {% attr form.martial_status 'group' class append %}inline{% endattr %}
    {% endform %}
    """)

    buttons = Template("""
        <button class="btn btn-primary pull-right" type="submit">Save application</button>
    """)

    title = "Personal Bank Account Initial Application"

    css = """
    .section h5 {
        font-size: 1.2rem;
        padding-bottom: 0.2rem;
        border-bottom: 3px solid black;
    }
    """

    blockclass = "col s12 m12 l9 offset-l1"
