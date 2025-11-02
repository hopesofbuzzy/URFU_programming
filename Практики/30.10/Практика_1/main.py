import requests

# Совершаем запрос для списка 20 покемонов
params = {'limit': 20}
response = requests.get('https://pokeapi.co/api/v2/pokemon/', params)

if response.status_code == 200:
    # Отображаем список покемонов
    results = response.json()["results"]
    print('Список первых 20 покемонов')
    for i, pokemon in enumerate(results):
        print(f'{i+1}. {pokemon["name"]}', end="\n")

    # Даём возможность обратиться
    # к определённому покемону по номеру index
    # Делаем запрос
    index = int(input('\nВведите номер для подробной информации: '))
    search_response = requests.get(
        f'https://pokeapi.co/api/v2/pokemon/{index}'
    )
    search_results = search_response.json()

    # Выводим результат поиска
    print('\nРезультат поиска:')
    print(f'Имя: {search_results["name"]}')
    types = [
        typed["type"]["name"] for typed in search_results['types']
    ]
    print(f'Тип: {", ".join(types)}')
    print(f'Вес: {search_results["weight"]}')
    print(f'Рост: {search_results["height"]}')
    abilities = [
        abilityd['ability']['name'] for abilityd in search_results['abilities']
    ]
    print(f'Способности: {", ".join(abilities)}')
    moves = [
        moved['move']['name'] for moved in search_results['moves']
    ]
    print(f'Ходы: {", ".join(moves)}')
