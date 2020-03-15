from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import AlbumModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            return render(request, 'signup.html', {'error': 'このユーザー名は既に登録されています。別のユーザー名を使用してください。'})
        except:
            user = User.objects.create_user(username, '', password)
            return redirect('login')
    return render(request, 'signup.html')


def login_func(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'error': 'ユーザー名またはパスワードが違います'})
    return render(request, 'login.html')


@login_required
def list_func(request):
    object_list = AlbumModel.objects.all().order_by('-update')
    return render(request, 'list.html', {'object_list': object_list})


@login_required
def detail(request, pk):
    object = AlbumModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})


@login_required
class CreatePost(CreateView):
    template_name = 'create.html'
    model = AlbumModel
    fields = ('author', 'title', 'image_01', 'memo_01', 'image_02', 'memo_02', 'image_03', 'memo_03')
    success_url = reverse_lazy('list')
