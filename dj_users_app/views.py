from django.shortcuts import render

# Create your views here.
def hello_users_world_view(request):
    return render(request, 'hello_users_world.html')