# Generated by Django 5.1.2 on 2024-11-03 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_category_post_categories_alter_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(default='padrão', related_name='posts', to='posts.category'),
        ),
    ]