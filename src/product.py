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

class Smartphone(Product):
    def __init__(self,name,description, price, quantity, efficiency, model, memory, color):
         super().__init__(name,description,price,quantity)
         self.efficiency = efficiency
         self.model = model
         self.memory = memory
         self.color = color

class LawnGrass(Product):
    def __init__(self,name, description, price, quantity, country, germination_period, color):
        super().__init__(name,description,price,quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

def __add__(self, other):
    if type(self) is not type(other):
        raise TypeError(
            f"Нельзя складывать товары разных классов: "
            f"{type(self).__name__} и {type(other).__name__}"
        )
    full_cost = self.price * self.quantity
    other_full_cost = other.price * other.quantity
    return full_cost + other_full_cost

