# Generated by Django 5.1.6 on 2025-02-25 14:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_servies'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintexts',
            name='servicesHeader',
            field=ckeditor.fields.RichTextField(default='none', verbose_name='Servies Header'),
        ),
    ]
