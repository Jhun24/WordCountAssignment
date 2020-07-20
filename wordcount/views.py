# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request,'home.html')

def result(request):
    text = request.GET['text']
    text_list = text.split()
    text_list_length = len(text_list)
    text_dic = {}

    for text_data in text_list:
        if(text_data in text_dic):
            text_dic[text_data] += 1
        else:
            text_dic[text_data] = 1

    return render(request,'result.html',{'text':text,'length':text_list_length,'dic':text_dic.items()})

def blog(request):
    return render(request,'blog.html',{'blog':Blog.objects})

def post(request):
    return render(request,'post.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/')