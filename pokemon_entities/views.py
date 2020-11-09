import folium
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = (55.751244, 37.618423)
ZOOM_START = 12
request = HttpRequest()
request.META['SERVER_NAME'] = '127.0.0.1'
request.META['SERVER_PORT'] = '8000'


def add_pokemon(folium_map, lat, lon, name, image_url, **kwargs):  # noqa: WPS211
    """Добавление покемонов на карту."""
    popup = ''
    for title, mark in kwargs.items():  # noqa: WPS519
        popup += f'<b>{title}: {mark}</b><br>'  # noqa: WPS336

    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
        popup=folium.Popup(popup, max_width=100),
    ).add_to(folium_map)


def show_all_pokemons(request):  # noqa: WPS442
    """Рендеринг всех покемонов и сущностей."""
    pokemons = Pokemon.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=ZOOM_START)
    pokemons_on_page = []

    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url if pokemon.image else None,
            'title_ru': pokemon.title,
        })

        pokemons_entities = PokemonEntity.objects.filter(pokemon=pokemon)
        # Можно и так, а как лучше? pokemons_entities = pokemon.pokemon_entities.all()
        image_url = request.build_absolute_uri(pokemon.image.url)
        for pokemon_entity in pokemons_entities:
            add_pokemon(
                folium_map,
                pokemon_entity.lat,
                pokemon_entity.lon,
                pokemon.title,
                image_url,
                Health=pokemon_entity.health,
                Level=pokemon_entity.level,
                Strength=pokemon_entity.strength,
                Defence=pokemon_entity.defence,
                Stamina=pokemon_entity.stamina,
            )

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),  # noqa: WPS437
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):  # noqa: WPS442
    """Рендеринг запрошенного покемона и его сущностей."""
    requested_pokemon = get_object_or_404(Pokemon, id=int(pokemon_id))

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=ZOOM_START)
    requested_pokemon_entities = requested_pokemon.pokemon_entities.all()
    image_url = request.build_absolute_uri(requested_pokemon.image.url)
    for pokemon_entity in requested_pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon_entity.pokemon.title,
            image_url,
            Health=pokemon_entity.health,
            Level=pokemon_entity.level,
            Strength=pokemon_entity.strength,
            Defence=pokemon_entity.defence,
            Stamina=pokemon_entity.stamina,
        )

    next_evolution_pokemon = requested_pokemon.next_evolution.first()

    pokemon_elements = requested_pokemon.element_type.all()
    element_type = []
    if pokemon_elements:
        for element in pokemon_elements:
            element_type.append(
                {
                    'title': element.title,
                    'img': element.image.url,
                    'strong_against': [
                        _.title for _ in element.strong_against.all()
                    ],
                },
            )

    pokemon = {
        'title_ru': requested_pokemon.title,
        'title_en': requested_pokemon.title_en,
        'title_jp': requested_pokemon.title_jp,
        'description': requested_pokemon.description,
        'img_url': requested_pokemon.image.url,
        'next_evolution': {
            'title_ru': next_evolution_pokemon.title,
            'pokemon_id': next_evolution_pokemon.id,
            'img_url': next_evolution_pokemon.image.url,
        } if next_evolution_pokemon else '',
        'previous_evolution': {
            'title_ru': requested_pokemon.previous_evolution.title,
            'pokemon_id': requested_pokemon.previous_evolution.id,
            'img_url': requested_pokemon.previous_evolution.image.url,
        } if requested_pokemon.previous_evolution else '',
        'element_type': element_type,
    }
    return render(
        request,
        'pokemon.html',
        context={
            'map': folium_map._repr_html_(),  # noqa: WPS437
            'pokemon': pokemon,
        },
    )
