from django.urls import path
from .views import index, signup, login_func, list_func, detail, CreatePost

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login_func, name='login'),
    path('list/', list_func, name='list'),
    path('detail/<int:pk>', detail, name='detail'),
    path('create/', CreatePost, name='create'),
]
