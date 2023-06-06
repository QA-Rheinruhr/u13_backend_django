from django.urls import path
from. import views

urlpatterns = [
    # tutorial
    path('team_app/', views.team_app, name='team_app'),
    path('team_app/details/<int:id>', views.details, name='details'),
    
    # own urls
    # URL für index definieren
    # home
    path('', views.index, name='index'),
    # ihk
    path('ihk11/', views.ihk11, name='ihk11'),
    path('ihk12/', views.ihk12, name='ihk12'),
    path('ihk13/', views.ihk13, name='ihk13'),
    path('ihk14/', views.ihk14, name='ihk14'),
    path('ihk15/', views.ihk15, name='ihk15'),
    # UML
    path('uml11/', views.uml11, name='uml11'),
    path('uml12/', views.uml12, name='uml12'),
    path('uml13/', views.uml13, name='uml13'),
    path('uml14/', views.uml14, name='uml14'),
    path('uml21/', views.uml21, name='uml21'),
    path('uml22/', views.uml22, name='uml22'),
    path('uml23/', views.uml23, name='uml23'),
    path('uml24/', views.uml24, name='uml24'),
    # GitHub
    path('github11/', views.github11, name='github11'),
    path('github12/', views.github12, name='github12'),
    path('github13/', views.github13, name='github13'),
    path('github14/', views.github14, name='github14'),
    path('github15/', views.github15, name='github15'),
    # Django 
    path('django11/', views.django11, name='django11'),
    path('django12/', views.django12, name='django12'),
    path('django13/', views.django13, name='django13'),
    path('django14/', views.django14, name='django14'),
    path('django15/', views.django15, name='django15'),
    path('django16/', views.django16, name='django16'),
]
