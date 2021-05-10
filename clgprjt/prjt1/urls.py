from django.urls import path
from . import views


urlpatterns=[
    
    path('insta',views.insta,name='insta'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('check',views.check,name='check'),
    path('post',views.post,name='post'),
    path('answ',views.answ,name='answ'),
     path('post_question',views.post_question,name='post_question'),
    path('answer',views.answer,name='answer'),
    ]