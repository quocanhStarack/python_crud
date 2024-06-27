from django.urls import path

from . import views

urlpatterns = [
    path('candidate', views.CandidateListView.as_view(), name='list-candidates'),
    path('candidate/<int:pk>', views.CandidateUpdateAndDeleteView.as_view()),
       path('candidate/<int:pk>', views.CandidateDetailView.as_view,name='detail'),
]