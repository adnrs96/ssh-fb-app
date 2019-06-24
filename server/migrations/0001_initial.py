# Generated by Django 2.2.2 on 2019-06-24 16:05

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=32, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(upload_to='profile_pics')),
                ('access_token', models.CharField(max_length=200)),
                ('is_active', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
