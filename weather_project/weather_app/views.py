from django.shortcuts import render

def index(request):
    return render(request, 'weather_template.html')

    
