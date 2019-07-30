from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Post


# def index(request):
#     post_list = Post.objects.order_by('post_publish_date')
#     template = loader.get_template('SocialBoard/index.html')
#     context = {
#         'post_list': post_list,
#     }
#     response = template.render(context, request)
#     return HttpResponse(response)


def index(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'SocialBoard/index.html', {'posts': posts})
