from django.urls import path
from job_list import views

urlpatterns = [
    # path('recent-posts/', views.recent_blog_posts, name="recent_posts"),
    # path('blog-post/<int:blog_post_id>', views.blog_post_view, name='blog_post'),
    # path('add-blog-post/', views.add_blog_post),
    # path('edit-blog-post/<int:blog_post_id>/', views.edit_blog_post, name='edit_blog_post'),
    path('recent-posts/', views.job_recent_blog_posts, name='job_recent_posts'),
    path('post/<int:job_post_id>', views.job_post_view, name='job_blog_post'),
    path('add-blog-post/', views.add_job_post),
    path('edit-job-post/<int:job_post_id>/', views.edit_job_post, name='edit_job_post'),
]

    
    