#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image as Img
from io import BytesIO
import uuid
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile


class School(models.Model):
    school_id = models.AutoField(primary_key=True)

    title = models.TextField()
    started = models.DateField()
    finished = models.DateField()
    description = models.TextField()
    major = models.TextField()

    class Meta:
        ordering = ['-started']


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)

    title = models.TextField()
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-from_date']

    @property
    def paragraphs(self):
        return self.description.split("\r\n\r\n\r\n")

    def save(self, *args, **kwargs):
        if self.image:
            img = Img.open(BytesIO(self.image.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((self.image.width/1.5,self.image.height/1.5), Img.ANTIALIAS)
            output = BytesIO()
            img.save(output, format='JPEG', quality=80)
            output.seek(0)
            self.image = InMemoryUploadedFile(output, 'ImageField', "{}.jpg".format(uuid.uuid4().hex), 'image/jpeg', output.tell(), None)
        super().save(*args, **kwargs)
