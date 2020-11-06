# Generated by Django 2.2.3 on 2020-11-06 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_auto_20201106_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, default='default'),
            preserve_default=False,
        ),
    ]