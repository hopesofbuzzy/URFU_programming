class Vehicle:
    def __init__(self, data):
        """
        Класс для транспортного средства
        """
        self.data = data


class Car(Vehicle):
    def info(self):
        """
        Возвращает информацию о машине
        """
        return f"Информация о машине: {self.data}"


class Bus(Vehicle):
    def info(self):
        """
        Возвращает информацию об автобусе
        """
        return f"Информация о автобусе: {self.data}"


class Train(Vehicle):
    def info(self):
        """
        Возвращает информацию о поезде
        """
        return f"Информация о поезде: {self.data}"


def vehicle_info(vehicle: Vehicle):
    """
    Обрабатывает запросы на информацию о транспортном средстве

    :param vehicle: транспортное средство
    """
    return vehicle.info()


car = Car("Личное мобильное транспортное средство")
bus = Bus("Общественное транспортное средство на колёсах")
train = Train("Транспортное средство на рельсах")

print(vehicle_info(train))
