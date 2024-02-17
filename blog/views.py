from django.shortcuts import redirect, render
from .models import Post


def test(request):
    return render(request, 'test.html', {'name': 'Jack', 'numbers': [1, 2, 3]})


def home(request):
    return render(request, 'home.html')

def form(request):
    return render(request, 'form.html')

def post_create(request):
    if request.method == "GET":
        return render(request, 'post/create.html')
    elif request.method == "POST":
        post = Post(title=request.POST["title"], content=request.POST["content"])
        post.save()
        return redirect("home")
    

def post_list(request):
    posts = Post.objects.all()
    return render(request, "post/list.html", {"posts": posts})

def post_show(request, id):
    post = Post.objects.get(pk=id)
    return render(request, "post/show.html", {"post": post})


def post_update(request, id):
    if request.method == "GET":
        post = Post.objects.get(pk=id)
        return render(request, "post/update.html", {"post": post})
    elif request.method == "POST":
        post = Post.objects.update_or_create(pk=id, defaults={
            "title": request.POST["title"],
            "content": request.POST["content"],
        })
        return redirect('home')
    

def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')