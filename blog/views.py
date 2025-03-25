from django.shortcuts import render, get_object_or_404, redirect
from .models import Post 
from .forms import PostForm

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
