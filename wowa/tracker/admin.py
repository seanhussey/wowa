#-*- coding:utf-8 -*-
"""
    tracker.admin
    ~~~~~~~~~~~~~~

    tracker admin file

    :copyright: (c) 2014 by arruda.
"""
from __future__ import absolute_import

from django.contrib import admin

from .models import Item


admin.site.register(Item, admin.ModelAdmin)
