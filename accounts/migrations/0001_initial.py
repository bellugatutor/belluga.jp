# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=40, verbose_name='phone number', blank=True)),
                ('card_type', models.CharField(max_length=100, verbose_name='credit card type', blank=True)),
                ('card_number', models.CharField(max_length=40, verbose_name='credit card number', blank=True)),
                ('card_name', models.CharField(max_length=200, verbose_name='name with card', blank=True)),
                ('expiration_date', models.DateField(null=True, verbose_name='expiration date', blank=True)),
                ('is_tutor', models.BooleanField(default=False, verbose_name='is tutor')),
                ('nationality', models.CharField(max_length=40, verbose_name='nationality', blank=True)),
                ('speak_japanese', models.CharField(default=b'yes', max_length=40, verbose_name='speak Japanese', choices=[(b'yes', 'Yes'), (b'a little', 'A little'), (b'no', 'No')])),
                ('photo', models.ImageField(upload_to=b'accounts', verbose_name='profile picture', blank=True)),
                ('intro_text', models.CharField(help_text='It will show up on the search page.', max_length=400, verbose_name='profile(200 words or less)', blank=True)),
                ('intro_text2', models.TextField(help_text='It will show up on your profile page.', max_length=2000, verbose_name='profile(1000 words or less)', blank=True)),
                ('intro_video', models.FileField(upload_to=b'accounts', verbose_name='introductory video', blank=True)),
                ('language', models.CharField(default=b'English', max_length=40, verbose_name='which language', choices=[(b'English', 'English'), (b'Chinese', 'Chinese'), (b'Korean', 'Korean')])),
                ('hourly_rate', models.PositiveIntegerField(default=2000, verbose_name='hourly rate', choices=[(2000, b'2000 JPY'), (2500, b'2500 JPY'), (3000, b'3000 JPY'), (3500, b'3500 JPY'), (4000, b'4000 JPY'), (4500, b'4500 JPY'), (5000, b'5000 JPY'), (5500, b'5500 JPY'), (6000, b'6000 JPY'), (6500, b'6500 JPY'), (7000, b'7000 JPY'), (7500, b'7500 JPY'), (8000, b'8000 JPY')])),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=500, verbose_name='location name')),
                ('tutor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(verbose_name='time')),
                ('location_name', models.CharField(max_length=500, verbose_name='location name')),
                ('student_show', models.BooleanField(default=True, verbose_name=b'student show up')),
                ('tutor_show', models.BooleanField(default=True, verbose_name=b'turor show up')),
                ('hourly_rate', models.PositiveIntegerField(verbose_name='hourly rate', blank=True)),
                ('student', models.ForeignKey(related_name=b'got_sessions', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(related_name=b'gave_sessions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(verbose_name='time')),
                ('tutor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
