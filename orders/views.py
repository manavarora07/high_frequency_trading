from django.http import HttpResponse

def index(request):
    return HttpResponse("Orders App is working!")
