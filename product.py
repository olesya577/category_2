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
        return f"Product({self.name}, {self.description}, {self.price}, {self.quantity})"


