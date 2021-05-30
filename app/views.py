from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from django.core import serializers
import traceback
from django.http import HttpResponse,JsonResponse
from django.views import View
from .tweet_helper import fetch_tweets

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
        
class Oxygen(View):
    
    def get(self,request):
        query = request.GET.get('query', 'covid oxygen');
        data = fetch_tweets(query)
        return render(request, 'resources.html', {'type' : 'oxygen', 'page_title' : 'Oxygen Availability Leads on Twitter' , 'data': data['data']})
        
class Plasma(TemplateView):
    def get(self,request):
        query = request.GET.get('query', 'covid blood plasma');
        data = fetch_tweets(query)
        return render(request, 'resources.html', {'type' : 'plasma', 'page_title' : 'Plasma Availability Leads on Twitter' , 'data': data['data']})
        
class Beds(TemplateView):
    def get(self,request):
        query = request.GET.get('query', 'covid beds');
        data = fetch_tweets(query)
        return render(request, 'resources.html', {'type' : 'beds', 'page_title' : 'Beds Availability Leads on Twitter' , 'data': data['data']})
        
class Medicines(TemplateView):
    def get(self,request):
        query = request.GET.get('query', 'covid medicines');
        data = fetch_tweets(query)
        return render(request, 'resources.html', {'type' : 'medicines', 'page_title' : 'Medicines Availability Leads on Twitter' , 'data': data['data']})
        
class Donation(TemplateView):
    def get(self,request):
        return render(request, 'donation.html', {'page_title' : 'Covid Helpers Organization'})

class Guidelines(TemplateView):
    def get(self,request):
        return render(request, 'faq.html', {'page_title' : 'Covid Related FAQ'})
        
class CaseTracker(TemplateView):
    def get(self,request):
        return render(request, 'covid_tracker.html', {'page_title' : 'Covid Case Tracker'})