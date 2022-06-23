from django.urls import path
from .views import EntryListView, EntryDetailView, EntryCreateView, EntryUpdateView, EntryDeleteView

urlpatterns = [
    path("", EntryListView.as_view(), name="entry-list"),
    path("entry/<int:pk>", EntryDetailView.as_view(), name="entry-detail"),
    path("entry/create", EntryCreateView.as_view(), name="entry-create"),
    path("entry/<int:pk>", EntryUpdateView.as_view(), name="entry-update"),
    path("entry/<int:pk>", EntryDeleteView.as_view(), name="entry-delete"),
]
