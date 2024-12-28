from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/recipies/all', views.all_recipies, name='all_recipies'),
    path('api/test/<int:start>/<int:end>/', views.tester, name='tester'),
]
