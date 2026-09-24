from tests.conftest import reset_category_counters,sample_category
from src.product import Product, Product_
from src.category import Category
import pytest


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


class TestProduct_:
    """Тесты для класса Product_"""

    def test_product_creation(self, sample_product):
        """Создание продукта"""
        assert sample_product.name == "Samsung Galaxy S23 Ultra"
        assert sample_product.description == "256GB, Серый цвет, 200MP камера"
        assert sample_product.price == 180000.0
        assert sample_product.quantity == 5

    def test_product_price_getter(self, sample_product):
        """Геттер цены"""
        assert sample_product.price == 180000.0

    def test_product_price_setter_valid(self, sample_product):
        """Установка валидной цены"""
        sample_product.price = 200000.0
        assert sample_product.price == 200000.0


    def test_product_price_setter_negative(self, sample_product, capsys):
        """Установка отрицательной цены"""
        old_price = sample_product.price
        sample_product.price = -100

        # Цена не должна измениться
        assert sample_product.price == old_price

        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_product_price_setter_multiple_attempts(self, sample_product, capsys):
        """Несколько попыток установки невалидной цены"""
        sample_product.price = 800
        assert sample_product.price == 800

        sample_product.price = -100
        assert sample_product.price == 800  # Не изменилась

        sample_product.price = 0
        assert sample_product.price == 800  # Не изменилась

        captured = capsys.readouterr()
        assert captured.out.count("Цена не должна быть нулевая или отрицательная") == 2


class TestCategory_:
    """Тесты для класса Category_"""

    def test_category_products_property(self, sample_category):
        """Свойство products"""
        products = sample_category.products

        assert isinstance(products, list)
        assert len(products) == 3
        assert products[0].name == "Samsung Galaxy S23 Ultra"

    def test_category_product_count_property(self, sample_category):
        """Свойство product_count"""
        assert sample_category.product_count == 3


class TestNewProduct:
    """Тесты для метода new_product"""

    def test_new_product_creation(self):
        """Создание продукта через new_product"""
        product_data = {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }

        new_product = Product_.new_product(product_data)

        assert new_product.name == "Samsung Galaxy S23 Ultra"
        assert new_product.description == "256GB, Серый цвет, 200MP камера"
        assert new_product.price == 180000.0
        assert new_product.quantity == 5

    def test_new_product_is_product_instance(self):
        """new_product возвращает объект Product"""
        product_data = {
            "name": "Test",
            "description": "Test Description",
            "price": 100.0,
            "quantity": 1,
        }

        new_product = Product_.new_product(product_data)

        assert isinstance(new_product, Product_)

    def test_new_product_missing_keys(self):
        """new_product с отсутствующими ключами"""
        product_data = {"name": "Test"}

        new_product = Product_.new_product(product_data)

        assert new_product.name == "Test"
        assert new_product.description is None
        assert new_product.price is None
        assert new_product.quantity is None

    def test_new_product_empty_dict(self):
        """new_product с пустым словарём"""
        new_product = Product_.new_product({})

        assert new_product.name is None
        assert new_product.description is None
        assert new_product.price is None
        assert new_product.quantity is None
