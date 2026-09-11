import pytest
from tests.conftest import reset_category_counters
from src.product import Product
from src.category import Category


class TestExampleScenario:
    """Тесты Product и Category"""

    @pytest.mark.usefixtures("reset_category_counters")
    def test_example_products_creation(self):
        product1 = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        assert product1.name == "Samsung Galaxy S23 Ultra"
        assert product1.description == "256GB, Серый цвет, 200MP камера"
        assert product1.price == 180000.0
        assert product1.quantity == 5

        assert product2.name == "Iphone 15"
        assert product2.price == 210000.0
        assert product2.quantity == 8

        assert product3.name == "Xiaomi Redmi Note 11"
        assert product3.price == 31000.0
        assert product3.quantity == 14

    @pytest.mark.usefixtures("reset_category_counters")
    def test_example_category_creation(self):
        """Проверка счетчика Product"""
        product1 = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        category1 = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product1, product2, product3],
        )

        assert category1.name == "Смартфоны"
        assert len(category1.products) == 3
        assert Category.category_count == 1
        assert Category.product_count == 3

    @pytest.mark.usefixtures("reset_category_counters")
    def test_example_second_category(self):
        """Проверка счетчика Category"""
        product1 = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        category1 = Category(
            "Смартфоны",
            "Описание смартфонов",
            [product1, product2, product3],
        )

        product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

        category2 = Category(
            "Телевизоры",
            "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            [product4],
        )

        assert category2.name == "Телевизоры"
        assert len(category2.products) == 1
        assert Category.category_count == 2
        assert Category.product_count == 4

    @pytest.mark.usefixtures("reset_category_counters")
    def test_example_counters(self):
        """Проверка счетчиков"""
        product1 = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

        category1 = Category("Смартфоны", "Описание", [product1, product2, product3])
        category2 = Category("Телевизоры", "Описание", [product4])

        # Проверка счетчика
        assert Category.category_count == 2
        assert Category.product_count == 4


class TestEdgeCases:

    @pytest.mark.usefixtures("reset_category_counters")
    def test_very_high_price(self):
        """Очень высокая цена"""
        product = Product("Name", "Desc", 999999999999.99, 10)

        assert product.price == 999999999999.99


    @pytest.mark.usefixtures("reset_category_counters")
    def test_very_large_quantity(self):
        """Очень большое количество"""
        product = Product("Name", "Desc", 100.0, 999999999)

        assert product.quantity == 999999999
