class Product:
    def __init__(self, price, discount, availability, category):
        """
        Класс для товара

        :param price: цена товара
        :param discount: скидка на товар
        :param availability: доступность
        :param category: категория
        """
        self.price = price
        self.discount = discount
        self.availability = availability
        self.category = category

    def __str__(self):
        """
        Регулирует строчный вывод товара
        """
        return (
            f"\nProduct - price:"
            f"{self.price}, discount: {self.discount}%, availability: {self.availability}, category: {self.category}"
        )


class ShoppingCart:
    def __init__(self, products):
        """
        Класс тележки со списком продуктов
        :param product:
        """
        self.products = products

    def add(self, product):
        """
        Добавляет продукт в список

        :param product: продукт
        """
        self.products.append(product)

    def remove(self, product):
        """
        Убирает продукт из списка

        :param product: продукт
        """
        self.products.remove(product)


class Customer:
    def __init__(self, email, password, cash):
        """
        Класс покупателся с данными и историей покупок

        :param email: почта покупателя
        :param password: незашифрованные пароль покупателя
        :param cash: счёт покупателя
        """
        self.email = email
        self.password = password
        self.cash = cash
        self.history = []

    def print_history(self):
        """
        Выводит историю покупателя
        """
        for order in self.history:
            print(
                f"Order_ You paid {order.overall_price} for:"
                f"{''.join(map(str, order.shopping_cart.products))}\n"
                f"Tax (for overall payment): {order.tax}%\n"
            )


class Order:
    def __init__(self, customer, shopping_cart, tax):
        """
        Класс для заказа покупателя с тележкой

        :param customer: покупатель
        :param shopping_cart: тележка
        :param tax: налог
        """
        self.customer = customer
        self.shopping_cart = shopping_cart
        self.tax = tax
        self.overall_price = 0

    def pay(self):
        """
        Процесс оплаты заказа с возвращением результата оплаты
        """
        self.overall_price = sum(
            [
                product.price * (1 - (product.discount / 100))
                for product in self.shopping_cart.products
                if product.availability
            ]
        )
        self.overall_price += self.overall_price * (self.tax / 100)
        if self.customer.cash >= self.overall_price:
            self.customer.cash -= self.overall_price
            self.customer.history.append(self)
            return (
                f"Success! You paid {self.overall_price} for:"
                f"{''.join(map(str, self.shopping_cart.products))}\n"
                f"Tax (for overall payment): {self.tax}%\n"
                f"Your current cash: {self.customer.cash}"
            )
        else:
            return "Your payment was rejected! Not enough cash!"


my_cart = ShoppingCart([Product(500, 50, True, "food"), Product(150, 0, True, "food")])
my_user = Customer("my_email5@yandex.ru", "ILoveTV", 603)
my_order = Order(my_user, my_cart, 50)
print(my_order.pay())
# my_user.print_history()
