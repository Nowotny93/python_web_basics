# Generated by Django 3.1.5 on 2022-01-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_auto_20220114_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
