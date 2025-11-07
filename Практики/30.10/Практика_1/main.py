import requests


def print_pokemons_list(limit: int):
    """
    Совершаем запрос на вывод списка покемонов

    :param limit: количество покемонов для вывода
    """
    # Совершаем запрос
    params = {'limit': limit}
    response = requests.get('https://pokeapi.co/api/v2/pokemon/', params)
    if response.status_code == 200:
        # Отображаем список покемонов
        results = response.json()["results"]
        print(f'Список первых {limit}  покемонов')
        for i, pokemon in enumerate(results):
            print(f'{i+1}. {pokemon["name"]}')


def print_pokemon(index: str):
    """
    Вывод информации об определённом покемоне

    :param name: имя или индекс покемона,
    для  которого выводим информациию
    """
    # Обращаемся к определённому 
    # покемону по номеру index
    # Делаем запрос
    search_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{index}')
    search_results = search_response.json()

    if search_response.status_code == 200:
    # Выводим результат поиска
        print('Результат поиска:')
        print(f'Имя: {search_results["name"]}')
        types = [typed["type"]["name"] for typed in search_results['types']]
        print(f'Тип: {", ".join(types)}')
        print(f'Вес: {search_results["weight"]}')
        print(f'Рост: {search_results["height"]}')
        abilities = [
            abilityd['ability']['name'] for abilityd in search_results['abilities']
        ]
        print(f'Способности: {", ".join(abilities)}')
        moves = [moved['move']['name'] for moved in search_results['moves']]
        print(f'Ходы: {", ".join(moves)}')


print_pokemons_list(5)
print_pokemon(input('Введите номер или имя покемона для подробной информации: '))