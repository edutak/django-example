from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Article
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm()
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'articles/detail.html', context)

@require_POST
@login_required
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')

@login_required
def update(request, pk):
    # 수정시에는 해당 article 인스턴스를 넘겨줘야한다!
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form': form
        }
        return render(request, 'articles/form.html', context)
    else:
        # 1. 메시지프레임워크를 사용하여, 메인페이지로 이동.
        messages.warning(request, '본인 글만 수정 가능합니다.')
        return redirect('articles:index')
        # 2. 403 status code를 반환.
        # return HttpResponseForbidden()

# @login_required
@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
        return redirect('articles:detail', article.pk)
    else:
        # 1. next parameter 없이 진행.
        messages.warning(request, '댓글 작성을 위해서는 로그인이 필요합니다.')
        return redirect('accounts:login')
        # return HttpResponse(status=401)