# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from ..operations import CreateDynamicModels


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0001_initial')
    ]

    operations = [
        CreateDynamicModels()
    ]
