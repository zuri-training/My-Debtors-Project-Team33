from django.urls import path
from schema_graph.views import Schema

urlpatterns = [
  path("Schema/", Schema.as_view()),
]
