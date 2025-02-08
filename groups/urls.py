from django.urls import path
from . import views


app_name = 'groups'


urlpatterns = [
    path('list/', views.GroupListView.as_view(), name='groups_list'),
    path('create/', views.GroupCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.GroupUpdateView.as_view(), name='update'),
    path('create/<int:pk>/', views.GroupDetailView.as_view(), name='detail'),
    path('create/<int:pk>/', views.GroupDeleteView.as_view(), name='delete'),
]