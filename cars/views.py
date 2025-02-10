from django.shortcuts import render
from django.http import HttpResponse
from .models import Carv
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
      return render(request,'car/index.html',{'car':Carv.objects.all()})


@login_required
def about(request):
      return render(request,'car/about.html')

@login_required
def contact(request):
      return render(request,'car/contact.html')