# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Restaurant(models.Model):

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
