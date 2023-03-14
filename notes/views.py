from .models import Notes
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/notes/'
    template_name = 'notes/notes_delete.html'
    context_object_name = 'note'


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/notes/'
    template_name = 'notes/notes_form.html'
    form_class = NotesForm
    extra_context = {'submit_btn': 'Update'}


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/notes/'
    template_name = 'notes/notes_form.html'
    form_class = NotesForm
    extra_context = {'submit_btn': 'Create'}

    def __init__(self, **kwargs):
        super().__init__()
        self.object = None

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notes/list.html'
    context_object_name = 'notes'
    login_url = '/login/'

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notes/detail.html'
    context_object_name = 'note'
