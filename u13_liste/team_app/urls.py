from django.urls import path
from. import views

urlpatterns = [
    # tutorial
    path('team_app/', views.team_app, name='team_app'),
    path('team_app/details/<int:id>', views.details, name='details'),
    
    # own urls
    # URL für index definieren
    path('', views.index, name='index'),
    path('ihk11/', views.ihk11, name='ihk11'),
]
