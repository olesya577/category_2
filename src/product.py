from typing import Dict,Any
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
        self.price = price
        self.quantity = quantity


    def __repr__(self):
        """Метод для информативного отображения"""
        return (
            f"Product({self.name}, {self.description}, {self.price}, {self.quantity})"
        )


class Product_:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, value: float):
        """
        Сеттер для цены с валидацией.
        Если цена <= 0, выводит предупреждение и не меняет цену.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> 'Product_':
        return cls(
            name=product_data.get('name'),
            description=product_data.get('description'),
            price=product_data.get('price'),
            quantity=product_data.get('quantity')
        )

    def __repr__(self) -> str:
        return f"Product({self.name}, {self.price}, {self.quantity})"