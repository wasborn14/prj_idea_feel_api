from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title

class Task(models.Model):

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=5000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title