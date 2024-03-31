from . import views
from django.urls import path,include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.getData),
    path('register/', views.registration_view, name='registration_view'),
    path('login/', views.login_view, name='login_view'),
    path('user/', views.user_profile, name='user_profile'),
    path('user/update/', views.update_profile, name='update_profile'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('all_blogs/', views.all_blogs, name='all_blogs'),
    path('user_blogs/', views.user_blogs, name='user_blogs'),
    path('all_categories/', views.all_categories, name='all_categories'),

    path('category/<str:category_id>/',
         views.blogs_by_category, name='blogs_by_category'),
    path('blog/<str:blog_id>/', views.blog_detail, name='blog_detail'),

    # Password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    # New views for comments, likes, and dislikes
    path('blog/<str:blog_id>/add_comment/',
         views.add_comment, name='add_comment'),
    path('blog/<str:blog_id>/like/', views.like_blog, name='like_blog'),
    path('blog/<str:blog_id>/dislike/', views.dislike_blog, name='dislike_blog'),

    path('blog/<str:blog_id>/get_likes/', views.get_likes, name='get_likes'),
    path('blog/<str:blog_id>/get_dislikes/',
         views.get_dislikes, name='get_dislikes'),
    path('blog/<str:blog_id>/get_comments/',
         views.get_comments, name='get_comments'),
    path('blog/<str:blog_id>/get_likes_count/',
         views.get_likes_count, name='get_likes_count'),
    path('blog/<str:blog_id>/get_dislikes_count/',
         views.get_dislikes_count, name='get_dislikes_count'),
    path('blog/<str:blog_id>/get_comments_count/',
         views.get_comments_count, name='get_comments_count'),


]
