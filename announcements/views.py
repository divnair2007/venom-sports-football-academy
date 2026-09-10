from django.views.generic import ListView, DetailView
from .models import Announcement


class AnnouncementListView(ListView):
    queryset = Announcement.objects.filter(is_published=True)
    template_name = "announcements/announcement_list.html"
    context_object_name = "announcements"


class AnnouncementDetailView(DetailView):
    queryset = Announcement.objects.filter(is_published=True)
    template_name = "announcements/announcement_detail.html"
    context_object_name = "announcement"
