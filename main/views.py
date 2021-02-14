from django.shortcuts import render, redirect 
from .forms import ArticleForm
from .models import Article 
# Create your views here.

def articles_list(request):
    articles = Article.objects.all( )
    context = {
        "articles": articles,
    }
    return render(request, "articles_list.html", context)

def article_details(request, article_id):
    context = {
        "article": Article.objects.get(id=article_id)
    }
    
    return render(request, 'article_details.html', context)

def article_create(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user 
            article.save()
            return redirect('article_details', article.id)
    context = {"form": form }

    return render(request, 'article_create.html', context)

def article_edit(request, article_id):
    article = Article.objects.get(id=article_id)

    form = ArticleForm(instance=article)
    if request.method == "POST":
        # Fill the form
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles-detail', article.id)

    context = {"form": form, "article": article}
    return render(request, 'article_edit.html', context)