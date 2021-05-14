from django.shortcuts import render, redirect

def wall(request):
    return render(request, 'thewall/wall.html')