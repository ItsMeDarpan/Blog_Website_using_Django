from django.shortcuts import render, get_object_or_404, redirect
from .models import Post 
from .forms import PostForm, signUpForm, searchForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts":posts})

def post_detail(request, pk):
    postDetail = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"postDetail":postDetail})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
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
    
def search(request):
    form = searchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = Post.objects.filer(name_icontains = query)

    return render(request, 'your_template.html', {'form':form, 'results':results})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('homepage')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, ' Login successfull')
    return redirect('login')        

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Here you would typically send an email or save to database
        # For now, we'll just show a success message
        messages.success(request, "Thank you for your message! We'll get back to you soon.")
        return redirect('contact')
    return render(request, 'contact.html')
        
@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def settings(request):
    if request.method == 'POST':
        # Handle profile information update
        if 'username' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            
            if User.objects.filter(username=username).exclude(id=request.user.id).exists():
                messages.error(request, 'Username already exists.')
            else:
                request.user.username = username
                request.user.email = email
                request.user.save()
                messages.success(request, 'Profile information updated successfully.')
        
        # Handle password change
        elif 'current_password' in request.POST:
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            
            if not request.user.check_password(current_password):
                messages.error(request, 'Current password is incorrect.')
            elif new_password != confirm_password:
                messages.error(request, 'New passwords do not match.')
            else:
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request, 'Password changed successfully.')
                return redirect('login')
        
        # Handle preferences update
        elif 'email_notifications' in request.POST:
            # Here you would typically save these preferences to a user profile model
            messages.success(request, 'Preferences updated successfully.')
    
    return render(request, 'settings.html')
        
@login_required
def dashboard(request):
    user_posts = Post.objects.filter(author=request.user)
    total_posts = user_posts.count()
    total_comments = 0  # You can add comment functionality later
    total_likes = 0    # You can add like functionality later
    
    context = {
        'user_posts': user_posts,
        'total_posts': total_posts,
        'total_comments': total_comments,
        'total_likes': total_likes,
    }
    return render(request, 'dashboard.html', context)

        

        
