from django.shortcuts import render
import django.http
# Create your views here.

def index(request):
	return HttpResponse("Katharine, welcome back! Coding is always here")