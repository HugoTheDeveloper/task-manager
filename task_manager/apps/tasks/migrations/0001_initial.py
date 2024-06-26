# Generated by Django 5.0.2 on 2024-03-13 12:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labels', '0001_initial'),
        ('statuses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('label', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    to='labels.label')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=255,
                                          unique=True)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(blank=True,
                                               null=True,
                                               on_delete=django.db.models.deletion.PROTECT, # noqa
                                               related_name='tasks_todo',
                                               to=settings.AUTH_USER_MODEL)),
                ('label_set', models.ManyToManyField(
                    through='tasks.Membership',
                    to='labels.label')),
                ('status', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    to='statuses.status')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='task',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to='tasks.task'),
        ),
    ]
