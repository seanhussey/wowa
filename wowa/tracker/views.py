# -*- coding: utf-8 -*-
"""
    tracker.views
    ~~~~~~~~~~~~~~

    tracker views file

    :copyright: (c) 2014 by arruda.
"""
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from annoying.decorators import render_to
