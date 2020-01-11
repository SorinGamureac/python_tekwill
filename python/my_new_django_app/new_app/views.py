from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from django import forms
import datetime
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse, JsonResponse, StreamingHttpResponse
from time import sleep
import os
from .models import BlogPost
from django.urls import reverse
from new_app.forms import BlogPostForm


@csrf_exempt
def my_first_view(request):
    #uploaded_file = request.FILES.get('my_file')
    #print(uploaded_file.read())
    return HttpResponse("hello world")

def second_view(request):
    time_data = datetime.date.today()
    return HttpResponse(time_data)



def days_until_new_year(request):
    days_ = datetime.date(2019,12,31) - datetime.date.today()
    return HttpResponse(days_)

# def mounth_view(request, year, mounth, title):
#     retunr HttpResponse(f'Year is {year} , {mounth}, {title}')

def cat_image_view(request):
    return FileResponse(open('cat.jpeg', 'rb'))

# def streaming_writer(rows):
#     for row in range(rows)
#         yield row
#         sleep(0.5)
# def streaming_view(request):
#     return streamingHttpResponse(streaming_writer)

def test_json(request):
    return JsonResponse({'name': 'Alice', 'age':22} )

def streaming_writer(number):
    for row in range(number):
        yield datetime.datetime.now('%m/%d/%Y') + "<br>"
        sleep(1)
def streaming_view(request):
    return StreamingHttpResponse(streaming_writer(50))

def random_number(request):
    rand = str(random.randint(1,100))
    return HttpResponse(rand)

def scan_dir(request):
    pwd = os.getcwd()
    content = os.listdir('.')
    list_f = []
    for f in content:
        list_f.append(f)
    outer = "<br>".join(list_f)
    return HttpResponse(outer)

@csrf_exempt
def post_request(request):
    #if request.method=="POST":
    print(request.POST)
    inputtxt=request.POST
    print(inputtxt)
    return HttpResponse(inputtxt)

def return_scheme_path(request):
    schem = request.scheme
    print(request.scheme)
    #link_path = HttpRequest.path
    return HttpResponse(schem)

@csrf_exempt
def save_hard(request):
    f = request.FILES['file']
    print(f)
    with open('my_csv.csv', 'wb') as destination:
        destination.write(f.read())
    return HttpResponse("succes")

    ##----------------------------------

def recent_blog_posts(request):
    blog_posts = \
        BlogPost.objects.all().order_by('-date_published')
    #response = ' <br>'.join([b.content for b in blog_posts])
    return render(request, 'blog_posts.html', {'recent_blog_posts': blog_posts})



def blog_post_view(request, blog_post_id):
    blog_post = BlogPost.objects.get(id=blog_post_id)
    return render(request, 'blog_post_page.html', {'blog_post': blog_post})

def add_blog_post(request):
    if request.method == 'GET':
        form = BlogPostForm
        return render(request, 'add_blog_post.html', {'form':form})

    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if forms.is_valid():
            form.save()
    return render(request, 'add_blog_post.html')

def edit_blog_post(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    edit_form = BlogPostForm(instance=blog_post)
    if request.method == 'POST':
        edit_form = BlogPostForm(request.POST, instance=blog_post)
        if edit_form.is_valid():
            edit_form.save()
            return redirect(reverse(blog_post_view, args=(blog_post_id, )))
        return render(request, 'edit_blog_post'), ('edit_form')
    else:
        edit_form = BlogPostForm(instance=blog_post)
        return render(request, 'edit_blog_post.html', {'form': edit_form, 'blog_post':
    blog_post})


