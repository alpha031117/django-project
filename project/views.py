from django.shortcuts import render
from django.http import HttpResponse
from app_blog.models import Post, Comment, Tag, Series

def home(request):
    context = {}
    context['blogs'] = Post.objects.all()
    context['tags'] = Tag.objects.all()
    context['comment'] = Comment.objects.all()
    context['series'] = Series.objects.all()
    
    return render(request, 'project/home.html', context=context)