# Generated by Django 3.2.7 on 2021-09-25 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('text', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('note', models.TextField()),
                ('tags', models.ManyToManyField(to='task.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('note', models.TextField()),
                ('tags', models.ManyToManyField(to='task.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('hours', models.DecimalField(decimal_places=1, max_digits=4)),
                ('note', models.TextField()),
                ('tags', models.ManyToManyField(to='task.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]