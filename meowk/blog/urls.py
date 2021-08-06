from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name="home"),
    path('post/<str:pk>', views.post, name="post"),

    path('register-user/', views.register_user, name='register-user'),
    path('login-user/', views.login_user, name='login-user'),
    path('logout-user/', views.logout_user, name='logout-user'),

    path('create-post/', views.create_post, name='create-post'),
    path('update-post/<str:pk>/', views.update_post, name='update-post'),
    path('delete-post/<str:pk>/', views.delete_post, name='delete-post'),
]
