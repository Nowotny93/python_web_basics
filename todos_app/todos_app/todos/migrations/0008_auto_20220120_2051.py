# Generated by Django 3.1.5 on 2022-01-20 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_todo_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='text',
            new_name='title',
        ),
    ]
