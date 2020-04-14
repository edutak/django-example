from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm

# from .forms import CustomUserChangeForm
# from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 게시글 목록 페이지
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)
