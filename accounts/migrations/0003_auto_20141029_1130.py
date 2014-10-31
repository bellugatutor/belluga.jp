# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20141016_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='area',
            field=models.CharField(default=b'Shibuya/Shinjuku', max_length=100, verbose_name='area', choices=[(b'Shibuya/Shinjuku', 'Shibuya/Shinjuku')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='prefecture',
            field=models.CharField(default=b'Tokyo', max_length=100, verbose_name='prefecture', choices=[(b'Tokyo', 'Tokyo'), (b'Kanagawa', 'Kanagawa'), (b'Chiba', 'Chiba'), (b'Saitama', 'Saitama'), (b'Osaka', 'Osaka'), (b'Kyoto', 'Kyoto'), (b'Hyogo', 'Hyogo')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='card_type',
            field=models.CharField(blank=True, max_length=100, verbose_name='credit card type', choices=[(b'JCB', 'JCB'), (b'MasterCard', 'MasterCard'), (b'VISA', 'VISA')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(default=b'English', max_length=40, verbose_name='which language', choices=[(b'English', 'English'), (b'Chinese', 'Chinese'), (b'Korean', 'Korean'), (b'German', 'German')]),
        ),
    ]
