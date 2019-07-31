from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


@login_required
def index(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        raise Http404("does not exist")
    return render(request, 'SocialBoard/index.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {'form': form, })


def logout(request):
    return render(request, "registration/logout.html")


@csrf_protect
def newpost(request):
    content = request.POST.get("content")
    title = request.POST.get("title")
    author = request.POST.get("author")
    Post.objects.create(post_title=title, post_publish_date=timezone.now(), post_author=author, post_content=content)
    posts = Post.objects.all()
    return render(request, 'SocialBoard/newpost.html', {'posts': posts})
