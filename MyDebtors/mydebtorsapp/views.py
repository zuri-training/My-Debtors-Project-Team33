from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect

# import views here
from django.views.generic import ListView, View

# import models here
from .models import School, Student, Comment
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .forms import StudentForm


# Create your views here.

# Homepage View
class HomeView(ListView):
  model = School
  template_name = 'partials/home.html'

  # def get_context_data(self, *args, **kwargs):
  #   school_list = School.objects.all()
  #   context = super(HomeView, self).get_context_data(*args, **kwargs)
  #   context["school_list"] = school_list
  #   return context

  
class DashboardView(ListView):
  model = Student
  template_name = 'users/dashboard.html'

  # def get_context_data(self, *args, **kwargs):
  #   school_list = School.objects.all()
  #   context = super(HomeView, self).get_context_data(*args, **kwargs)
  #   context["school_list"] = school_list
  #   return context

class CommentView(ListView):
  model = Comment
  template_name = ''


# class AboutView(View):
#   template_name = 'AboutUs/aboutus.html'


def debtors_form(request):
  if request.method == "POST":
    form = StudentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('about_debtors')
  else:
    form = StudentForm()
  
  context = {
    'form' : form 
  }
  return render(request, 'about_us_debtors_form/debtors_form1.html', context)

# class AboutView(View):
#   template_name = 'AboutUs/aboutus.html'


def aboutPage(request):
  reverse_lazy('home')
  return render(request, 'AboutUs/aboutus.html')


def blogView(request):
  return render(request, 'blog-page/blog.html')


def contactUsView(request):
  return render(request, 'contact-us-page/contactus.html')