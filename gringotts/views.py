from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.core import serializers
from gringotts.forms import NameForm
import json 


def home(request):
	form = NameForm()
	return render(request, 'index.html', {'form': form})


def get_data(request):
	print request.POST
	return HttpResponse(status=201)