# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse, get_resolver

@login_required
def home(request):
	context = {
	}
	mtext = "Welcome"
	messages.success(request, mtext)
	return render(request, 'home.html', context)
