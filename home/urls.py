from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('sad/', views.sad, name='sad'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('page4/', views.page4, name='page4'),
    path('romantic/', views.romantic, name='romantic'),
    path('rom_pg2/', views.rom_page2, name='rompg2'),
    path('rom_pg3/', views.rom_page3, name='rompg3'),
    path('rom_pg4/', views.rom_page4, name='rompg4'),
    path('urdu/', views.urdu, name='urdu'),
    path('urdu_pg2/', views.urdu_pg2, name='urdu_pg2'),
    path('girl/', views.girl, name='girl'),
     
]
