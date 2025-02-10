from django.urls import path
from . import views

<<<<<<< HEAD

app_name = 'subjects'


=======
app_name = 'subjects'

>>>>>>> 9727532 (Hatola hali kop)
urlpatterns = [
    path('list/', views.SubjectListView.as_view(), name='subject_list'),
    path('create/', views.SubjectCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.SubjectUpdatedView.as_view(), name='update'),
<<<<<<< HEAD
    path('detail/<int:pk>/', views.SubjectDetailView.as_view(), name='detail'),
=======
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.SubjectDetailView.as_view(), name='detail'),
>>>>>>> 9727532 (Hatola hali kop)
    path('delete/<int:pk>/', views.SubjectDeleteView.as_view(), name='delete'),
]