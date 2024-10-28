from django.urls import path
from . import views

urlpatterns = [
    path('', views.bosh_sahifa, name='bosh_sahifa'),
    path('fakultet-haqida/', views.fakultet_haqida, name='fakultet_haqida'),
    path('kurslar/', views.kurslar, name='kurslar'),
    path('yangiliklar/', views.yangiliklar, name='yangiliklar'),
    path('kafedralar/', views.kafedralar, name='kafedralar'),
]
