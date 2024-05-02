from django.urls import path

from app.views import (
    AboutView,
    HomepageView,
    NewsDetailView,
    NewsListView,
    TicketCreateView,
)

urlpatterns = [
  	path("", HomepageView.as_view(), name="home"),
  	path("about/", AboutView.as_view(), name="about"),

  	path("news/", NewsListView.as_view(), name="news-list"),
  	path("news/<uuid:pk>/", NewsDetailView.as_view(), name="news"),

  	path("ticket/", TicketCreateView.as_view(), name="ticket-create"),
]