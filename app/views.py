from django.views.generic import CreateView, DetailView, ListView, TemplateView

from app.models import News, Ticket


class HomepageView(TemplateView):
    template_name = "homepage.html"


class AboutView(TemplateView):
    template_name = "about.html"


class NewsListView(ListView):
    model = News
    paginate_by = 100
    template_name = "news-list.html"
    ordering = '-created_at'
    context_object_name = "news_list"


class NewsDetailView(DetailView):
    model = News
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = "news.html"
    context_object_name = "news"


class TicketCreateView(CreateView):
    model = Ticket
    template_name = "ticket.html"
    success_url = "/"
    fields = ["name", "phone"]