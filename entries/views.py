from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Entry


class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-created_on")


class EntryDetailView(DetailView):
    model = Entry


class EntryCreateView(SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry_list")
    success_message = "New entry created"


class EntryUpdateView(SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Updated entry"

    def get_success_url(self):
        return reverse_lazy("entry_detail", kwargs={"pk": self.entry.id})


class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry_list")
    success_message = f"Deleted entry"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
