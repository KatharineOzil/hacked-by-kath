# Generated by Django 4.0.dev20210825111435 on 2021-08-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user_github_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avater',
            field=models.ImageField(default='blog/static/category_cover/default.png', upload_to='blog/static/others/'),
        ),
    ]
