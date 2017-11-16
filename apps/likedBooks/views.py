from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
  return render(request,'likedBooks/index.html')