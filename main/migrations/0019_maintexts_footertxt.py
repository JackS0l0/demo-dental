# Generated by Django 5.1.6 on 2025-02-25 15:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_maintexts_blogheader'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintexts',
            name='footertxt',
            field=ckeditor.fields.RichTextField(default='none', verbose_name='Footer bottom text'),
        ),
    ]
