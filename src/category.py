from src.product import Product
class Category:
    """Класс, который хранит информацию о категориях продуктов"""

    name: str
    description: str
    products: list
    product_count: int
    category_count: int
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        """Метод инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для доступа к приватному списку товаров."""
        result = ""
        for product in self.__products:
            line = f"{product.name}, {product.price:.0f} руб. Остаток: {product.quantity} шт.\n"
            result += line
        return result




