# Generated by Django 5.1.6 on 2025-02-25 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintexts',
            old_name='first_block_title',
            new_name='firstBlockTitle',
        ),
        migrations.RemoveField(
            model_name='maintexts',
            name='first_block_desc',
        ),
        migrations.RemoveField(
            model_name='maintexts',
            name='first_block_second_title',
        ),
    ]
