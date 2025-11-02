import requests
from random import randint


class Pokemon:
    """Класс для покемона с его характеристиками"""

    def __init__(self, index):
        """
        Инициализировать класс покемона

        :param index: индекс или имя, по которому по API достаётся
        информация о покемоне
        """
        # Ищем нужного покемона
        search_response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{index}"
        )
        search_results = search_response.json()
        # Присваиваем значения
        self.name = search_results["name"]
        self.types = [
            typed["type"]["name"] for typed in search_results["types"]
        ]
        self.weight = search_results["weight"]
        self.height = search_results["height"]
        self.abilities = [
            abilityd["ability"]["name"]
            for abilityd in search_results["abilities"]
        ]
        self.moves = [
            moved["move"]["name"] for moved in search_results["moves"]
        ]

    def __str__(self):
        """Вывсти покемона в строчном формате"""
        return (
            f"Имя: {self.name}, "
            f'Тип: {", ".join(self.types)}, '
            f"Вес: {self.weight}, "
            f"Рост: {self.height}, "
            f'Способности: {", ".join(self.abilities)}.'
        )


class Team:
    """Класс для команды с покемонами"""

    def __init__(self, *args):
        """
        Инициализировать класс команды покемонов

        :param *args: экземпляры покемонов для вступления
        в команду при создании команды
        """
        self.pokemons = list(args)

    def add(self, pokemon: Pokemon):
        """
        Добавить покемона в команду

        :param pokemon: экземпляр покемона для добавления
        """
        for p in self.pokemons:
            if p.name == pokemon.name:
                return
        self.pokemons.append(pokemon)

    def remove(self, name: str):
        """
        Удалить покемона из команды

        :param name: имя покемона для удаления
        """
        for p in self.pokemons:
            if p.name == name:
                self.pokemons.remove(p)

    def get_pokemon(self, name: str):
        """
        Получить покемона в команде по имени

        :param name: имя покемона для получения
        :return: найденный покемон или None
        """
        for pokemon in self.pokemons:
            if pokemon.name == name:
                return pokemon
        return None

    def print_info(self):
        """Вывести подробную информацию о команде"""
        print("\n".join([str(pokemon) for pokemon in self.pokemons]))

    def train(self, name1: str, name2: str):
        """
        Провести тренировочный бой двух покемонов

        :param name1: имя первого покемона
        :param name2: имя второго покемона
        """
        pokemon1 = self.get_pokemon(name1)
        pokemon2 = self.get_pokemon(name2)
        if pokemon1 is not None and pokemon2 is not None:
            print(f"Бой между {name1} и {name2}!")
            if randint(1, 2) == 1:
                print(f"Победил {name1}")
            else:
                print(f"Победил {name2}")
        else:
            print("Бой между покемонами не в команде невозможен!")


my_team = Team(Pokemon("golduck"), Pokemon("caterpie"), Pokemon("charmeleon"))
my_team.print_info()
my_team.add(Pokemon("pikachu"))
my_team.train("pikachu", "charmeleon")
my_team.remove("charmeleon")
my_team.print_info()
