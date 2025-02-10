<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import DeleteView, UpdateView
=======
from django.contrib import messages
from django.shortcuts import redirect

from .models import Student
from .forms import StudentForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
>>>>>>> 9727532 (Hatola hali kop)


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
<<<<<<< HEAD
    template_name = 'students/form.html'
    fields = ('first_name', 'last_name', 'birth_date', 'images', 'phone_number', 'grade', 'gender', 'enrollment_date')
    success_url = reverse_lazy('student_list')


class StudentUpdatedView(UpdateView):
    model = Student
    template_name = 'students/form.html'
    fields = ('first_name', 'last_name', 'birth_date', 'images', 'phone_number', 'grade', 'enrollment_date')
    success_url = reverse_lazy('student_list')
=======
    form_class = StudentForm
    template_name = 'students/form.html'
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        messages.success(self.request, "Student successfully created!")
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/form.html'
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        messages.success(self.request, "Student successfully updated!")
        return super().form_valid(form)
>>>>>>> 9727532 (Hatola hali kop)


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
<<<<<<< HEAD
    context_object_name = 'students'
=======
    context_object_name = 'student'
>>>>>>> 9727532 (Hatola hali kop)


class StudentDeleteView(DeleteView):
    model = Student
<<<<<<< HEAD
    template_name = 'students/list.html'
    success_url = reverse_lazy('student_list')
=======
    success_url = reverse_lazy('students:list')

    def dispatch(self, request, *args, **kwargs):
        group = self.get_object()
        group.delete()
        return redirect(self.success_url)
>>>>>>> 9727532 (Hatola hali kop)
