from django.urls import path
from schema_graph.views import Schema

# Import views here to render pages
from .views import HomeView, DashboardView, CommentView, AboutView
from . import views

urlpatterns = [
  path("Schema/", Schema.as_view()),
  path("", HomeView.as_view(), name='home'),
  # path("", PostView.as_view(), name='posts'),
  path("dashboard/", DashboardView.as_view(), name='dashboard'),
  path("comment/", CommentView.as_view(), name="comment"),
  path("dashboard/about/", AboutView.as_view(), name="about"),
  path("dashboard/about_debtors/", views.debtors_form, name="about_debtors"),
]
