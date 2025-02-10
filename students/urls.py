from django.urls import path
from . import views


app_name = 'students'


urlpatterns = [
    path('list/', views.StudentListView.as_view(), name='student_list'),
    path('create/', views.StudentCreateView.as_view(), name='create'),
<<<<<<< HEAD
    path('update/<int:pk>/', views.StudentUpdatedView.as_view(), name='update'),
    path('detail/<int:pk>/', views.StudentDetailView.as_view(), name='detail'),
=======
    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='update'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>', views.StudentDetailView.as_view(), name='detail'),
>>>>>>> 9727532 (Hatola hali kop)
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='delete'),
]