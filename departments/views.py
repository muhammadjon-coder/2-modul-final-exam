import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .models import Department
from subjects.models import Subject
from students.models import Student
from teachers.models import Teacher
from groups.models import Group
from .forms import DepartmentForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import DeleteView, UpdateView


class DashboardView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'dashboard.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['teachers'] = Teacher.objects.all()
        ctx['groups'] = Group.objects.all()
        ctx['subjects'] = Subject.objects.all()
        ctx['groups_count'] = Group.objects.filter(status='ac').count()
        ctx['subject_names'] = [subject.name for subject in Subject.objects.all()]
        ctx['subject_teachers_counts'] = [subject.teachers.count() for subject in Subject.objects.all()]
        ctx['subject_names_json'] = json.dumps(ctx['subject_names'])
        ctx['subject_teachers_counts_json'] = json.dumps(ctx['subject_teachers_counts'])
        return ctx


class DepartmentsListView(ListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'


class DepartmentsCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('departments:list')


class DepartmentsUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/form.html'
    success_url = reverse_lazy('departments:list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class DepartmentsDetailView(DetailView):
    model = Department
    template_name = 'departments/detail.html'
    context_object_name = 'department'


class DepartmentsDeleteView(DeleteView):
    model = Department
    success_url = reverse_lazy('departments:list')

    def dispatch(self, request, *args, **kwargs):
        group = self.get_object()
        group.delete()
        return redirect(self.success_url)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author