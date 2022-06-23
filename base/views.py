from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Category, Post
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PostForm


# Create your views here.
def home(request):
    # get all post data
    post_list = Post.objects.all()
    # get  category for list
    categories =Category.objects.all()[:10]

    paginator = Paginator(post_list, 9) # Show 9 contacts per page.

    #will force get page param, and you will get page=1 if not found 
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {
        'categories':categories,
        'posts':posts,
    }
    return render(request, 'home.html',context)
    
def about(request):
    # posts = Post.objects.all()
    return render(request, 'about.html')

def categorydetail(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category_id=category.id)
    categories = Category.objects.exclude(id=category.id)
    context = {
        'category':category,
        'posts':posts,
        'categories':categories,
    }
    return render(request, 'category_detail.html',context)

def signup(request):
    page = 'register'
    if request.method == 'GET':
        context = {'page':page}
        return render(request, 'login_register.html',context)
    else:
        u_name = request.POST['username']
        u_email = request.POST['email']
        p1 = request.POST['password']
        p2 = request.POST['confirm_password']
        if p1 == p2:
            try:
                u = User(username=u_name, email =u_email)
                u.set_password(p1)
                u.save()
            except:
                messages.add_message(request, messages.ERROR, "User Not Found")
                return redirect('signup')
        else:
            messages.add_message(request, messages.ERROR, "Passwords does not match")
            return redirect('signup')
        messages.add_message(request, messages.SUCCESS, "Login to continue your session")
        return redirect('signin')

       

def signin(request):
    if request.method == 'GET':
        page = 'login'
        context = {'page':page}
        return render(request, 'login_register.html',context)
    else:
        u_name = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=u_name, password=pwd)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Welcome!")
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Passwords and username does not match")
            return redirect('signin')
            
@login_required(login_url='signin')
def dashboard(request):
    return render(request, 'dashboard.html')

def signout(request):
    # logout
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def createpost(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Post created Successfully")
            return redirect('listpost')

    else:
        form = PostForm(request.POST or None, request.FILES or None)
        
        context ={
            'form':form
        }
    return render(request, 'create_post.html',context)

# post list
@login_required(login_url='signin')
def listpost(request):
    # get post data form model
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10) # Show 10 contacts per page.

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context ={
        'posts': posts
    }
    return render(request, 'list_post.html',context)

# editpost
@login_required(login_url='signin')
def editpost(request,id):
    # get data for edit
    data = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=data)
        
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Post Updated Successfully")
            return redirect('listpost')

    else:
        form = PostForm(request.POST or None, request.FILES or None, instance=data)

        context ={
            'form':form
        }
    
    return render(request, 'edit_post.html', context)

def deletepost(request, id):
    data = Post.objects.get(pk=id)
    data.delete()
    messages.add_message(request, messages.SUCCESS, "Post Deleted Successfully")
    return redirect('listpost')

def postdetail(request, slug):
    data = Post.objects.get(slug=slug)
    # data dict
    context ={
            'data':data
        }
    
    return render(request, 'post_detail.html', context)
