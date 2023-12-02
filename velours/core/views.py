from django.shortcuts import render

def HomeView(request):
    return render(request, 'core/index.html')
# Create your views here.
