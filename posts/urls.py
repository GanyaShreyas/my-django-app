from django.urls import path

from .import views
urlpatterns=[
 path('create/',views.post_create,name='create'),
 path('feed',views.feed,name='feed'),
 #path('posts/<int:pk>/', views.post_detail, name='post_detail'),
 path('like',views.like_post,name='like'),
 




]

""" 
<a class="nav-item py-2 px-4 text-blue-500 font-semibold hover:text-blue-700 transition duration-300" href="{% url 'edit' %}">PROFILE</a>
<a class="nav-item py-2 px-4 text-blue-500 font-semibold hover:text-blue-700 transition duration-300" href="{% url 'create' %}">CREATE</a>
<a class="nav-item py-2 px-4 text-blue-500 font-semibold hover:text-blue-700 transition duration-300" href="{% url 'edit' %}">MY POSTS</a>
<a class="nav-item py-2 px-4 text-blue-500 font-semibold hover:text-blue-700 transition duration-300" href="{% url 'feed' %}">FEEDS</a>
<a class="nav-item py-2 px-4 text-blue-500 font-semibold hover:text-blue-700 transition duration-300" href="{% url 'password_change' %}">CHANGE PASSWORD</a>
<button type="submit" class="nav-item py-2 px-4 text-blue-500 font-semibold hover:text-blue-700 transition duration-300">LOGOUT</button>


"""