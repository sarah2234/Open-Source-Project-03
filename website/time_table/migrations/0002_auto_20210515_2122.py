# Generated by Django 3.2.3 on 2021-05-15 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_table', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='content',
            new_name='_content',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='context_ellipsis',
            new_name='_context_ellipsis',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='name',
            new_name='_name',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='sort',
            new_name='_sort',
        ),
    ]
