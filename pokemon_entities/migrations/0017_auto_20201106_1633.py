# Generated by Django 2.2.3 on 2020-11-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0016_auto_20201106_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pokemons_img', verbose_name='Картинка'),
        ),
    ]
