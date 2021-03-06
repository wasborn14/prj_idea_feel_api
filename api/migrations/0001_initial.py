# Generated by Django 4.0.5 on 2022-07-14 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('content', models.CharField(max_length=5000, null=True, verbose_name='content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('icon_id', models.IntegerField(null=True, verbose_name='icon_id')),
                ('sort_id', models.IntegerField(null=True, verbose_name='sort_id')),
            ],
        ),
    ]
