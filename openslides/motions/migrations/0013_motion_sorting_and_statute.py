# Generated by Django 2.1.1 on 2018-09-24 08:26

import django.db.models.deletion
from django.db import migrations, models

import openslides.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('motions', '0012_motion_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='motionblock',
            options={
                'default_permissions': (),
                'verbose_name': 'Motion block'},
        ),
        migrations.AddField(
            model_name='motion',
            name='sort_parent',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='children',
                to='motions.Motion'),
        ),
        migrations.AddField(
            model_name='motion',
            name='weight',
            field=models.IntegerField(default=10000),
        ),
        migrations.CreateModel(
            name='StatuteParagraph',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('weight', models.IntegerField(default=10000)),
            ],
            options={
                'ordering': ['weight', 'title'],
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='motion',
            name='statute_paragraph',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='motions',
                to='motions.StatuteParagraph'),
        ),
    ]
