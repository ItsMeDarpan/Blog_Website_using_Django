from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required


#List all blog posts
def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html',{'posts':posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

# List all blog posts
def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

# View a single blog post
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})

# Create a new blog post (Only for staff)
@login_required
def create_post(request):
    if not request.user.is_staff:
        return redirect('blog_list')  # Redirect normal users

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign current user as author
            post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})