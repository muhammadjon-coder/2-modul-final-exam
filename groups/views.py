<<<<<<< HEAD
from .models import Group
from .forms import GroupForm
from django.urls import reverse_lazy
=======
from django.contrib import messages
from .models import Group
from .forms import GroupForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
>>>>>>> 9727532 (Hatola hali kop)
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import DeleteView, UpdateView


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/form.html'
<<<<<<< HEAD
    success_url = reverse_lazy('groups_list')

=======
    success_url = reverse_lazy('groups:list')

    def form_valid(self, form):
        print("form is valid")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_valid(form)
>>>>>>> 9727532 (Hatola hali kop)

class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/form.html'
<<<<<<< HEAD
    success_url = reverse_lazy('groups_list')
=======
    success_url = reverse_lazy('groups:list')

    def form_valid(self, form):
        messages.success(self.request, "Group successfully updated!")
        return super().form_valid(form)
>>>>>>> 9727532 (Hatola hali kop)


class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'
    context_object_name = 'groups'


class GroupDeleteView(DeleteView):
    model = Group
<<<<<<< HEAD
    template_name = 'groups/list.html'
    context_object_name = 'groups'
=======
    success_url = reverse_lazy('groups:list')

    def dispatch(self, request, *args, **kwargs):
        group = self.get_object()
        group.delete()
        return redirect(self.success_url)
>>>>>>> 9727532 (Hatola hali kop)
