from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    # POST /articles/new/ => (구) create 함수
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 검증하기
        if form.is_valid():
            # ModelForm 인스턴스를 저장하면,
            # 내부적으로 Article을 저장하고 해당하는 인스턴스를 반환한다.
            article = form.save()
            return redirect('articles:index')
    # GET /articles/new/
    else:
        form = ArticleForm()
    # context가 활용되는 경우
    # 1) GET 요청 : ArticleForm()
    # 2) POST 요청 + invalid : ArticleForm(request.POST)
    context = {
        'form': form
    }
    return render(request, 'articles/new.html', context)