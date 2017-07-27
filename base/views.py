#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views import generic as views
from honeypot.decorators import check_honeypot
from django.core.mail import EmailMessage


from . import forms
from .utils import get_upwork_data


class ContactUs(views.FormView):
    form_class = forms.ContactForm
    template_name = 'base/contact_form.html'
    success_url = '/'
    http_method_names = ['post']

    @method_decorator(check_honeypot)
    def dispatch(self, *args , **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        email = EmailMessage(
            _('Site message from ') + form.cleaned_data['name'],
            form.cleaned_data['message'],
            settings.SERVER_EMAIL,
            [settings.ADMINS[0][1]],
            reply_to=[form.cleaned_data['email']]
        )
        email.send()
        messages.success(self.request, _('Your message was sent successfully!'))
        return super().form_valid(form)

    def get_form(self, **kwargs):
        email = getattr(self.request.user, 'email', '')
        if email:
            self.initial['email'] = email
        return super().get_form(**kwargs)


class HomeView(views.TemplateView):
    template_name = 'base/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['contact_form'] = forms.ContactForm()
        context.update(get_upwork_data())
        context['dev_adj_score_recent'] /= 5
        context['score'] = int(round(context['dev_adj_score_recent']*100, 0))
        context['dev_billed_assignments'] = int(context['dev_billed_assignments'])

        context['stroke_dasharray'] = 289
        context['stroke_dashoffset'] = context['stroke_dasharray'] - context['stroke_dasharray']*context['dev_adj_score_recent']

        return context
