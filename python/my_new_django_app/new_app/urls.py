from django.urls import path
from new_app import views


urlpatterns = [
    path('', views.my_first_view),
    path('second/', views.second_view),
    path('my-cat/', views.cat_image_view),
    path('json/', views.test_json), 
    path('date-time/', views.streaming_view), 
    path('random_num/', views.random_number), 
    path('days_new_year/', views.days_until_new_year),
    path('scan/', views.scan_dir),
    path('post_link/', views.post_request),
    path('scheme_path/', views.return_scheme_path),
    path('save_hard/', views.save_hard),
    path('recent-posts/', views.recent_blog_posts, name="recent_posts"),
    path('blog-post/<int:blog_post_id>', views.blog_post_view, name='blog_post'),
    path('add-blog-post/', views.add_blog_post),
    path('edit-blog-post/<int:blog_post_id>/', views.edit_blog_post, name='edit_blog_post'),
    #path('job-recent-posts/', views.job_recent_blog_posts)
    
]

#, name="job_recent_posts")
    # path('job/blog-post/<int:blog_post_id>', views.job_blog_post_view, name='job_blog_post'),
    # path('job/add-blog-post/', views.job_add_blog_post),
    # path('job/edit-blog-post/<int:blog_post_id>/', views.job_edit_blog_post, name='job_edit_blog_post')