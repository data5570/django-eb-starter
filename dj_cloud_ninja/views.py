from django.shortcuts import render

def hello_world_view(request):
    return render(request, 'hello_world.html')