# -*- coding: utf-8 -*-
"""
    tracker.views
    ~~~~~~~~~~~~~~

    tracker views file

    :copyright: (c) 2014 by arruda.
"""
from __future__ import absolute_import

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from annoying.decorators import render_to

from allauth.account.adapter import get_adapter

from .models import Character
from .forms import CharacterForm


def tracked_items(request):
    pass


@login_required
@render_to('tracker/new_char.html')
def new_char(request):
    "create a character for the logged user"

    user = request.user

    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            new_char = form.save(commit=False)
            new_char.user = user
            new_char.save()
            get_adapter().add_message(request,
                                      messages.SUCCESS,
                                      'tracker/messages/char_created.txt',
                                      {'character': new_char})

            return redirect('profile')
    else:
        form = CharacterForm()
    return locals()
