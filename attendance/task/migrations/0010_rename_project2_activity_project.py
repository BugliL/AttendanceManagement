# Generated by Django 3.2.7 on 2021-09-30 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_auto_20210930_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='project2',
            new_name='project',
        ),
    ]
