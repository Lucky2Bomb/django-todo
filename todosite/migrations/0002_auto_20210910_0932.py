# Generated by Django 3.2.7 on 2021-09-10 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todosite', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoList',
            new_name='Todo',
        ),
        migrations.RenameField(
            model_name='tasktodo',
            old_name='todolist',
            new_name='todo',
        ),
    ]
