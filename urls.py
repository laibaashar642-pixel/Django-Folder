from django.urls import include, path
from .import views
urlpatterns = [
  
    path('recepie/', views.recepie, name='recepie'),

]