from django.urls import path
from schema_graph.views import Schema

# Import views here to render pages
from .views import HomeView, DashboardView, CommentView

urlpatterns = [
  path("Schema/", Schema.as_view()),
  path("", HomeView.as_view(), name='home'),
  # path("", PostView.as_view(), name='posts'),
  path("dashboard/", DashboardView.as_view(), name='dashboard'),
  path("comment/", CommentView.as_view(), name="comment"),
]
