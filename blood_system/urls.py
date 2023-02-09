from django.urls import path
from . import views



urlpatterns = [
    path('', views.home_page, name="home"),
    
    path('Who We Are/', views.about_us, name="who we are"),
    path('Blog/', views.blog, name="blog"),
    path('Contact/', views.contact, name="contact"),
    path('Chat/', views.chat, name="chat"),
    path('How it works/', views.how_it_works, name="how it works"),
    path('Post Request/', views.post_request, name="post request"),
    path('Register as Donor/', views.register, name="register"),
    path('room/<str:pk>/', views.room, name="room"),

    path('create-talk/',  views.create_talk, name="create-talk"),
    path('update-talk/<str:pk>/',  views.update_talk, name="update-talk"),
    path('delete-talk/<str:pk>/',  views.delete_talk, name="delete-talk"),

    



    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
   # path('delete-message/<str:pk/', views.delete_message, name="delete-message"),
]