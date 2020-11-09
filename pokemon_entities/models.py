from django.db import models


class PokemonElementType(models.Model):
    """Стихии покемонов."""

    title = models.CharField(verbose_name='Название', max_length=20)  # noqa: WPS432
    image = models.ImageField(verbose_name='Стихия картинка', upload_to='pokemons_elemnt_img')
    strong_against = models.ManyToManyField(
        'PokemonElementType',
        verbose_name='Силен против',
        symmetrical=False,
    )

    def __str__(self):
        """Название в админке."""
        return self.title


class Pokemon(models.Model):
    """Модель покемонов."""

    title = models.CharField(verbose_name='Название', max_length=200)  # noqa: WPS432
    title_en = models.CharField(verbose_name='Название на англ', max_length=200, blank=True)  # noqa: WPS432
    title_jp = models.CharField(verbose_name='Название на яп', max_length=200, blank=True)  # noqa: WPS432
    image = models.ImageField(verbose_name='Картинка', upload_to='pokemons_img')
    description = models.TextField(verbose_name='Описание', blank=True)
    previous_evolution = models.ForeignKey(
        'Pokemon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='next_evolution',
        verbose_name='Предок',
    )
    element_type = models.ManyToManyField(PokemonElementType, verbose_name='Стихия')

    def __str__(self):
        """Название в админке."""
        return self.title


class PokemonEntity(models.Model):
    """Сущности покемонов."""

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemon_entities')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Появится в', null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name='Исчезнет в', null=True, blank=True)
    level = models.IntegerField(verbose_name='Уровень', null=True, blank=True)
    health = models.IntegerField(verbose_name='Здоровье', null=True, blank=True)
    strength = models.IntegerField(verbose_name='Атака', null=True, blank=True)
    defence = models.IntegerField(verbose_name='Защита', null=True, blank=True)
    stamina = models.IntegerField(verbose_name='Выносливость', null=True, blank=True)

    def __str__(self):
        """Название в админке."""
        return f'{self.pokemon.title} сущность {self.id}'
