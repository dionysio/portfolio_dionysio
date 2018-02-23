#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import AutoField
from django.contrib import admin

from .models import Project, School


class AllFieldsAdmin(admin.ModelAdmin):
    @property
    def list_display(self):
        return [field.name for field in self.model._meta.fields if not isinstance(field, AutoField)]

    list_per_page = 20


class ProjectAdmin(AllFieldsAdmin):
    model = Project
    search_fields = ['title', 'description']


class SchoolAdmin(AllFieldsAdmin):
    model = School


for model, model_admin in ((Project, ProjectAdmin), (School, SchoolAdmin)):
    admin.site.register(model, model_admin)
