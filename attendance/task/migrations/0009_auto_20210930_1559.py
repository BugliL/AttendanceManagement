# Generated by Django 3.2.7 on 2021-09-30 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20210930_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='project',
        ),
        migrations.AlterField(
            model_name='activity',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='activities', to='task.event'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='project2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='activities', to='task.project2'),
        ),
    ]
