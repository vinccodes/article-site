from django.urls import path, include 

from main import views 

urlpatterns = [
    path('', views.articles_list, name="articles-list"),
    path('articles/<int:article_id>/', views.article_details, name="articles-detail"),
    path('create/', views.article_create, name="articles-create"),
    path('articles/<int:article_id>/edit', views.article_edit, name="articles-edit"),
]