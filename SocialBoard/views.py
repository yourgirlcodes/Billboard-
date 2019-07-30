from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


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


# def login(request):
#     return render(request, "registration/login.html")
#
