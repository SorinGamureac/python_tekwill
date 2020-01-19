from django.urls import path
from rest_app import views


urlpatterns = [
    path('fancy-cats/', views.FancyCatListView.as_view(), name='fancy-cat-list')
]