#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"placeholder": _("What's your name?"), "class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": _('Your email address'), "class": "form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": _('Hi Dio, here is my cool business idea...'), "class": "form-control"}))