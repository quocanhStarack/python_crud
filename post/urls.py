from django.urls import path

from . import views

urlpatterns = [
    path('post', views.PostView.as_view(), name='list-post'),
    path('post/id=<int:pk>', views.PostView.as_view(), name = 'detail-post'),
    path('post/<int:pk>', views.UpdateDeletePostView.as_view()),
]