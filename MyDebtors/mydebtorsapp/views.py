from multiprocessing import context
from django.shortcuts import render, get_object_or_404

# import views here
from django.views.generic import ListView

# import models here
from .models import School, Student, Comment
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# Create your views here.

# Homepage View
class HomeView(ListView):
  model = School
  template_name = 'navbar.html'

  # def get_context_data(self, *args, **kwargs):
  #   school_list = School.objects.all()
  #   context = super(HomeView, self).get_context_data(*args, **kwargs)
  #   context["school_list"] = school_list
  #   return context

  
class DashboardView(ListView):
  model = Student
  template_name = 'dashboard.html'

  # def get_context_data(self, *args, **kwargs):
  #   school_list = School.objects.all()
  #   context = super(HomeView, self).get_context_data(*args, **kwargs)
  #   context["school_list"] = school_list
  #   return context

class CommentView(ListView):
  model = Comment
  template_name = ''