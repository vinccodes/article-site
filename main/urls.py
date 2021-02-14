from django.urls import path, include 

from main import views 

urlpatterns = [
    path('', views.articles_list, name="articles-list"),
    path('articles/<int:article_id>/', views.article_details, name="article-detail"),
    path('create/', views.article_create, name="article-create"),
    path('articles/<int:article_id>/edit', views.article_edit, name="article-edit"),
    path('my-articles/', views.my_articles_list, name="my-articles-list"),
]