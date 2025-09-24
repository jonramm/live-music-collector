from django.urls import path
from . import views

urlpatterns = [
    path('', views.venue_list, name='venue_list'),

    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('venue/new/', views.venue_new, name='venue_new'),
    path('venue/<int:pk>/', views.venue_detail, name='venue_detail'),
    path('venue/<int:pk>/edit/', views.venue_edit, name='venue_edit'),
]