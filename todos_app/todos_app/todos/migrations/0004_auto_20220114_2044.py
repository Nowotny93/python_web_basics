# Generated by Django 3.1.5 on 2022-01-14 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20220114_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='categories',
            field=models.ManyToManyField(to='todos.Category'),
        ),
    ]