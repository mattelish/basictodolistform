from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Todo(models.Model):
    todo_text = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date')
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def __str__(self):              # __unicode__ on Python 2
       return self.todo_text