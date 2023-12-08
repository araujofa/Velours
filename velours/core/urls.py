from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='HomeView'),

    path('releases', views.ReleaseView, name='ReleaseView'),

    path('men', views.MasculineView, name='MasculineView'),

    path('women', views.FeminineView, name='FeminineView'),

    path('children', views.InfantView, name='InfantView'),

    path('offers', views.OfferView, name='OfferView'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)