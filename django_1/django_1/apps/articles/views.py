from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.urls import reverse

from .models import Article, Comment


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_data')[:5]
    return render(request, "articles/list.html", {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статтю не знайдено!")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request,  'articles/detail.html', {'article': a, 'latest_comments_list':latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статтю не знайдено!")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args = (a.id,)))


def test(request):
    return HttpResponse("Привіт світ!")
