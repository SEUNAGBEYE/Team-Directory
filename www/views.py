from django.shortcuts import render
from .models import Person

# Create your views here.

def index(request):
	peoples = Person.objects.all()
	return render(request, 'index.html', {'peoples': peoples}, )
