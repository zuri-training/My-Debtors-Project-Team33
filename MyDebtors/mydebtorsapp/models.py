import email
from statistics import mode
from django.db import models


# Create your models here.
class School(models.Model):
  school_name = models.CharField(max_length=100)
  school_admin = models.CharField(max_length=100)
  school_email = models.EmailField()
  school_address = models.CharField(max_length=100)
  school_location = models.CharField(max_length=100)
  school_phone_no = models.BigIntegerField()

  def __str__(self):
    return f"{self.school_name}"
  

class Student(models.Model):
  first_name = models.CharField(max_length=150)
  last_name = models.CharField(max_length=150)
  parent_name = models.CharField(max_length=200)
  parent_email = models.EmailField(max_length=100)
  parent_phone_no = models.BigIntegerField()
  address = models.CharField(max_length=200)
  location = models.CharField(max_length=100, default="XYZ")
  admission_no = models.CharField(max_length=12, unique=True)
  fees_owed = models.IntegerField()
  last_school = models.ForeignKey(School, on_delete=models.CASCADE, default=True)
  

  def __str__(self):
    return f"{self.first_name}"


class Comment(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='comments')
  name = models.CharField(max_length=80)
  email = models.EmailField()
  body = models.TextField(max_length=100)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
      ordering = ['created_on']

  def __str__(self):
    return 'Comment {} by {}'.format(self.body, self.name)
