from django.shortcuts import render

def HomeView(request):
    return render(request, 'core/index.html')

def ReleaseView(request):
    return render(request, 'core/release.html')

def InfantView(request):
    return render(request, 'core/infant.html')

def MasculineView(request):
    return render(request, 'core/masculine.html')

def FeminineView(request):
    return render(request, 'core/feminine.html')

def OfferView(request):
    return render(request, 'core/offer.html')
# Create your views here.
