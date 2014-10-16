# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='intro_text2',
            field=models.CharField(help_text='It will show up on your profile page.', max_length=2000, verbose_name='profile(1000 words or less)', blank=True),
        ),
    ]
