from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# in this file we can create and edit our databases


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)  #if a user is deleted then we want to delete thier posts as well


    def __str__(self):
        return self.title
























