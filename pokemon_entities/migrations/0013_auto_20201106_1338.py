# Generated by Django 2.2.3 on 2020-11-06 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_auto_20201106_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='parent',
            new_name='previous_evolution',
        ),
    ]