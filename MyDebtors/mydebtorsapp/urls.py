from django.urls import path
from schema_graph.views import Schema

# Import views here to render pages
from .views import HomeView

urlpatterns = [
  path("Schema/", Schema.as_view()),
  path("", HomeView.as_view(), name='home')
]
