from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Question(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,unique=False)
    quest=models.CharField(max_length=1000,unique=False)
    
    time=models.DateTimeField(default=datetime.now)

class Answer(models.Model):
    ques=models.OneToOneField(Question,on_delete=models.CASCADE,unique=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE,unique=False)
    an=models.CharField(max_length=1000,unique=False)
    
    time=models.DateTimeField(default=datetime.now)