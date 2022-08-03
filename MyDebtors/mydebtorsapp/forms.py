
from .models import Comment, Student, School
from django import forms

# Comment form
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name', 'email', 'body')


# Student form
class StudentForm(forms.ModelForm):
      class Meta:
            model = Student
            fields = ('first_name', 'last_name', 'parent_name', 
                      'parent_email', 'parent_phone_no', 'address', 
                      'location', 'admission_no', 'fees_owed', 'last_school')


# School form