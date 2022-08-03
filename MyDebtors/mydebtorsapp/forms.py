from pyexpat import model

from attr import fields
from .models import Comment, Student, School
from django import forms

# Comment form
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name', 'email', 'body')


# Student form




# School form