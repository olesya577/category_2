class Product:
    """Класс, который хранит информацию о продуктах"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        """Метод для информативного отображения"""
        return (
            f"Product({self.name}, {self.description}, {self.price}, {self.quantity})"
        )

    @property
    def price(self) -> float:
        """Геттер для получения значения приватной цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для установки новой цены с проверкой на положительность"""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """Класс-метод для создания экземпляра Product из словаря"""
        return cls(name=data["name"], description=data["description"], price=data["price"], quantity=data["quantity"])

    def __add__(self, other):
        if isinstance(other, Product):
            full_cost = self.price * self.quantity
            other_full_cost = other.price * other.quantity
            return full_cost + other_full_cost
        return NotImplemented