from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from django.core import serializers
import traceback

'''
This class will render home page for Sign Up/Login.
'''
class Home(TemplateView):
    try:
        template_name = 'index.html'
    except:
        template_name = '404.html'
    
class Vaccination(TemplateView):
    try:
        template_name = 'index.html'
    except:
        template_name = '404.html'
        
class Oxygen(TemplateView):
    try:
        template_name = 'index.html'
    except:
        template_name = '404.html'
        
class Plasma(TemplateView):
    try:
        template_name = 'index.html'
    except:
        template_name = '404.html'
        
class Beds(TemplateView):
    try:
        template_name = 'index.html'
    except:
        template_name = '404.html'
        
class Remdesivir(TemplateView):
    try:
        template_name = 'index.html'
    except:
        template_name = '404.html'
        
class Donation(TemplateView):
    try:
        template_name = 'index.html'
    except:
        template_name = '404.html'
        
class Guidelines(TemplateView):
    try:
        template_name = 'index.html'
    except:
        template_name = '404.html'
        
class CaseTracker(TemplateView):
    try:
        template_name = 'index.html'
    except:
        template_name = '404.html'