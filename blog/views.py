from django.shortcuts import render, get_object_or_404, redirect
from .models import Post 
from .forms import PostForm, signUpForm
from django.contrib.auth import login
from django.contrib.auth.models import User



def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts":posts})

def post_detail(request, pk):
    postDetail = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"postDetail":postDetail})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = PostForm()
    return render(request, 'create_post.html',{'form':form})

def update_post(request, pk):
    post = Post.objects.get(pk = pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = PostForm(instance = post)
    return render(request, 'create_post.html',{'form':form})
                
def delete_post(request, pk):
    post = Post.objects.get(pk = pk)
    if request.method == "POST":
        post.delete()
        return redirect('homepage')
    return render(request, 'post_delete.html', {'post':post})

def register(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = signUpForm()
        return render(request, 'signup.html', {'form': form})
    
