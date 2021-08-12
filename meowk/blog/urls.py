from django.urls import path
from .import views


urlpatterns = [
    path('register-user/', views.register_user, name='register-user'),
    path('login-user/', views.login_user, name='login-user'),
    path('logout-user/', views.logout_user, name='logout-user'),

    path('manage-post/<str:pk>/', views.manage_post, name="manage-post"),
    path('account-settings/',
         views.account_settings, name="account-settings"),

    path('', views.home, name="home"),
    path('post/<str:pk>/', views.post, name="post"),

    path('create-post/<str:pk>/', views.create_post, name='create-post'),
    path('update-post/<str:pk>/', views.update_post, name='update-post'),
    path('delete-post/<str:pk>/', views.delete_post, name='delete-post'),
]
