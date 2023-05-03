from django.http import HttpResponse
from django.shortcuts import render


def home_view (request):
   # return HttpResponse ('Hello world! aigain...')
   return render(request,'home.html')


 