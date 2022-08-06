from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm

from django.contrib.auth import authenticate, login


# Create your views here.
class UserRegisterView(generic.CreateView):
    # form_class = UserCreationForm
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')  # Send to login once registered or to home


class UserEditView(generic.UpdateView):
    # form_class = UserChangeForm
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        success_url = reverse_lazy('dashboard')
    else:
        # Return an 'invalid login' error message.
        success_url = reverse_lazy('dashboard')       

