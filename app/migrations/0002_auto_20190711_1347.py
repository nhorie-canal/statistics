# Generated by Django 2.2.3 on 2019-07-11 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='updated_date',
            new_name='update_date',
        ),
    ]
