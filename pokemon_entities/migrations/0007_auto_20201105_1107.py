# Generated by Django 2.2.3 on 2020-11-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20201105_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(default=None),
        ),
    ]
