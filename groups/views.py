from django.contrib import messages
from .models import Group
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView, UpdateView
from .forms import GroupForm
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy



class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/form.html'
    success_url = reverse_lazy('groups:list')

    def form_valid(self, form):
        print("form is valid")
        return super().form_valid(form)

def form_invalid(self, form):
    print(form.errors)
    return super().form_invalid(form)


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/form.html'
    success_url = reverse_lazy('groups:list')

    def form_valid(self, form):
        messages.success(self.request, "Group successfully created!")
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'
    context_object_name = 'group'


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, "Group successfully deleted!")
        return super().post(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        group = self.get_object()
        group.delete()
        return redirect(self.success_url)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author