from django.urls import path, include 

from main import views 
urlpatterns = [
    path('', views.articles_list, name="articles-list"),
]