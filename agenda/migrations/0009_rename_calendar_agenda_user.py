# Generated by Django 5.0.6 on 2024-07-21 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0008_remove_agenda_tasks_delete_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenda',
            old_name='calendar',
            new_name='user',
        ),
    ]