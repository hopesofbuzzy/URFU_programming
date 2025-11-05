import requests


class Pokemon:
    """Класс для покемона с его характеристиками"""

    def __init__(self, index):
        """
        Инициализировать класс покемона

        :param index: индекс или имя, по которому по API достаётся
        информация о покемоне
        """
        # Ищем нужного покемона
        search_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{index}")
        search_results = search_response.json()
        # Присваиваем значения
        self.name = search_results["name"]
        self.types = [typed["type"]["name"] for typed in search_results["types"]]
        self.weight = search_results["weight"]
        self.height = search_results["height"]
        self.abilities = [
            abilityd["ability"]["name"] for abilityd in search_results["abilities"]
        ]
        self.moves = [moved["move"]["name"] for moved in search_results["moves"]]
        for stat in search_results["stats"]:
            stat_name = stat["stat"]["name"]
            if stat_name == "hp":
                self.hp = int(stat["base_stat"])
            elif stat_name == "attack":
                self.attack = int(stat["base_stat"])
            elif stat_name == "defense":
                self.defense = int(stat["base_stat"])
        # Значения для биты
        self.fight_hp = self.hp

    def __str__(self):
        """Вывсти покемона в строчном формате"""
        return (
            f"Имя: {self.name}, "
            f"Тип: {', '.join(self.types)}, "
            f"Вес: {self.weight}, "
            f"Рост: {self.height}, "
            f"Способности: {', '.join(self.abilities)} "
            f"Здоровье: {self.hp} "
            f"Атака: {self.attack} "
            f"Защита: {self.defense}."
        )

    def attack_enemy(self, enemy):
        """
        Атаковать покемона с силой self.attack

        :param enemy: покемон для атаки
        """
        return enemy.get_damage(self.attack)

    def get_damage(self, attack):
        """
        Получить урон силой max(attack//2, attack - self.defense)

        :param attack: сила атаки
        """
        self.fight_hp -= max(attack // 2, attack - self.defense)
        return max(attack // 2, attack - self.defense)

    def rest(self):
        """Дать Покемону отдохнуть, чтобы он восполнил силы"""
        self.fight_hp = self.hp


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


def train(pokemon1: Pokemon, pokemon2: Pokemon):
    """
    Провести тренировочный бой двух покемонов

    :param pokemon1: первый покемон
    :param pokemon2: второй покемон
    """
    if pokemon1 is not None and pokemon2 is not None:
        print("======================")
        print(f"Начинаем бой между {pokemon1.name} и {pokemon2.name}!")
        pokemons = [pokemon1, pokemon2]
        while all([pokemon.fight_hp > 0 for pokemon in pokemons]):
            print(
                f"Текущий баланс сил: {pokemon1.name} {pokemon1.fight_hp}/{pokemon2.fight_hp} {pokemon2.name}"
            )
            print(f"{pokemons[0].name} наносит удар силы {pokemons[0].attack}")
            print(f"{pokemons[1].name} теряет {pokemons[0].attack_enemy(pokemons[1])}")
            print("======================")
            pokemons.reverse()
        else:
            print(f"Победил {max(pokemons, key=lambda x: x.fight_hp).name}")
    else:
        print("Бой должен быть между покемончиками!")


my_team = Team(Pokemon("golduck"), Pokemon("caterpie"), Pokemon("charmeleon"))
my_team.add(Pokemon("pikachu"))

my_pikachu = my_team.get_pokemon("pikachu")
my_charmeleon = my_team.get_pokemon("charmeleon")
train(my_charmeleon, my_pikachu)

my_team.remove("charmeleon")
my_team.print_info()
