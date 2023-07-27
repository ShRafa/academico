from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'front/home.html', context)
