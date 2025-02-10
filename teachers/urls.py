from django.urls import path
from . import views


app_name = 'teachers'


urlpatterns = [
    path('list/', views.TeacherListView.as_view(), name='teacher_list'),
    path('create/', views.TeacherCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.TeacherUpdatedView.as_view(), name='update'),
<<<<<<< HEAD
    path('detail/<int:pk>/', views.TeacherDetailView.as_view(), name='detail'),
=======
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.TeacherDetailView.as_view(), name='detail'),
>>>>>>> 9727532 (Hatola hali kop)
    path('delete/<int:pk>/', views.TeacherDeleteView.as_view(), name='delete'),

]