from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#-----here we will fetch the data from url
#-----for exam we are providing the data in url and capturing the data from the url and use it in view
def Fetching_Data_URL(request,data):
    return HttpResponse(f'<center><h1 style="font-family:Arial">Data Fetched From URL - {data}</h1></center>')

