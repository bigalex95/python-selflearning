from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from django.urls import reverse

from .models import Article

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_article_list': latest_article_list})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except expression as identifier:
        raise Http404("Article Not Found!")

    latest_comment_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comment_list': latest_comment_list,})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except expression as identifier:
        raise Http404("Article Not Found!")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args = (a.id,)))