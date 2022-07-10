from django.db import models
from django.contrib.auth import get_user_model
# from users.models import User

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

class Memo(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    title = models.CharField(max_length=255, null=False, verbose_name='title')
    content = models.CharField(max_length=5000, null=True, verbose_name='content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')
    # TODO:下記とこちらどちらが良いのか確認： create_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作成者')
    create_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='作成者')

    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, \
        verbose_name='parent_id', related_name='child_memo')
    icon_id = models.IntegerField(null=True, verbose_name='icon_id')

    def __str__(self):
        return str(self.id) + " - " + self.title