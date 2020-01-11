from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, FileResponse, JsonResponse, StreamingHttpResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from .models import JobPost
from django.urls import reverse
from job_list.forms import JobPostForm
from time import sleep
import datetime
import random
import os
from django.shortcuts import redirect

# Create your views here.
# job_recent_blog_posts
# job_blog_post_view
# job_add_blog_post
# job_edit_blog_post

def job_recent_blog_posts(request):
    job_posts = \
        JobPost.objects.all().order_by('-date_published')
    # response = ' <br>'.join([b.content for b in job_posts])
    # return HttpResponse(response)
    return render(request, 'job_posts.html', {'job_recent_blog_posts': job_posts})

def job_post_view(request, job_post_id=1):
    job_post = JobPost.objects.get(id=job_post_id)
    return render(request, 'job_post_page.html', {'job_post': job_post})

def add_job_post(request):
    if request.method == 'GET':
        form = JobPostForm
        return render(request, 'add_job_post.html', {'form':form})

    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'add_job_post.html')

def edit_job_post(request, job_post_id):
    job_post = get_object_or_404(JobPost, pk=job_post_id)
    edit_form = JobPostForm(instance=job_post)
    if request.method == 'POST':
        edit_form = JobPostForm(request.POST, instance=job_post)
        if edit_form.is_valid():
            edit_form.save()
            return redirect(reverse(job_post_view, args=(job_post_id, )))
        return render(request, 'edit_job_post.html', {'edit_form': edit_form})
    else:
        edit_form = JobPostForm(instance=job_post)
        return render(request, 'edit_job_post.html', {'form': edit_form, 'job_post':
    job_post})