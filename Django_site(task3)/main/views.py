from django.shortcuts import render,redirect
from django.views.generic import DetailView, ListView, View
from .models import Post
from django.contrib import messages
from .forms import CreateUserForm, PostForm
from django.contrib.auth import authenticate, login, logout



class PostDetailView(DetailView):
    model = Post

class PostCreate(View):
    def get(self, request):
        form = PostForm
        return render(request, 'main/post_create.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'main/post_create.html', context={'form': bound_form})


class PostListView(ListView):
    model = Post


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was successfully created:)')

            return redirect('login')
    context = {'form':form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('posts:list')
    context = {}
    return render(request, 'accounts/login.html', context)


