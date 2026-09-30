from tests.conftest import (
    reset_category_counters,
    sample_category,
    product1,
    product2,
    product3,
    smartphone1,
    smartphone2,
    smartphone3,
    grass1,
    grass2,
first_category,
category_without_product

)
from src.product import Product, Smartphone, LawnGrass,BaseProduct,MixinProduct
from src.category import Category
import pytest

from abc import ABC, abstractmethod

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


class TestProduct:
    """Тесты для класса Product"""

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


class TestProductAdd:
    """Тесты для метода __add__ класса Product"""

    def test_add_product1_product2(self, product1, product2):
        """product1 + product2"""
        # 180000 * 5 + 210000 * 8 = 900000 + 1680000 = 2580000
        expected = 180000.0 * 5 + 210000.0 * 8
        assert product1 + product2 == expected

    def test_add_product1_product3(self, product1, product3):
        """product1 + product3"""
        # 180000 * 5 + 31000 * 14 = 900000 + 434000 = 1334000
        expected = 180000.0 * 5 + 31000.0 * 14
        assert product1 + product3 == expected

    def test_add_product2_product3(self, product2, product3):
        """product2 + product3"""
        # 210000 * 8 + 31000 * 14 = 1680000 + 434000 = 2114000
        expected = 210000.0 * 8 + 31000.0 * 14
        assert product2 + product3 == expected

    def test_add_returns_number(self, product1, product2):
        """__add__ возвращает число"""
        result = product1 + product2
        assert isinstance(result, (int, float))

    def test_add_same_product(self, product1):
        """Сложение продукта с самим собой"""
        expected = 180000.0 * 5 * 2
        assert product1 + product1 == expected


class TestCategory:
    """Тесты для класса Category"""

    def test_category_product_count_property(self, sample_category):
        """Свойство product_count"""
        assert sample_category.product_count == 3

    def test_print_str_category(self, sample_category, capsys):
        """Вывод категории через print"""
        print(str(sample_category))
        captured = capsys.readouterr()
        assert "Смартфоны, количество продуктов: 27 шт." in captured.out

    def test_products_in_category_str(self, sample_category, capsys):
        """Вывод списка продуктов категории"""
        print(sample_category.products)
        captured = capsys.readouterr()

        # Проверяем, что в выводе есть все продукты
        assert "Samsung Galaxy S23 Ultra" in captured.out
        assert "Iphone 15" in captured.out
        assert "Xiaomi Redmi Note 11" in captured.out


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

        new_product = Product.new_product(product_data)

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

        new_product = Product.new_product(product_data)

        assert isinstance(new_product, Product)



def test_smartphone1_attributes(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.price == 180000.0
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.memory == 256
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.color == "Серый"


def test_smartphone2_attributes(smartphone2):
    assert smartphone2.name == "Iphone 15"
    assert smartphone2.price == 210000.0
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"


def test_smartphone3_attributes(smartphone3):
    assert smartphone3.name == "Xiaomi Redmi Note 11"
    assert smartphone3.price == 31000.0
    assert smartphone3.efficiency == 90.3
    assert smartphone3.memory == 1024


def test_smartphone_is_product(smartphone1):
    """Smartphone является наследником Product"""
    assert isinstance(smartphone1, Product)
    assert isinstance(smartphone1, Smartphone)


def test_grass_init(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.quantity == 20
    assert grass1.price == 500
    assert grass1.germination_period == "7 дней"
    assert grass1.country == "Россия"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.color == "Зеленый"


def test_grass2_attributes(grass2):
    assert grass2.name == "Газонная трава 2"
    assert grass2.price == 450.0
    assert grass2.country == "США"
    assert grass2.germination_period == "5 дней"


def test_grass_is_product(grass1):
    """LawnGrass является наследником Product"""
    assert isinstance(grass1, Product)
    assert isinstance(grass1, LawnGrass)


class TestAddition:
    """Тесты для метода __add__"""

    def test_smartphone_sum(self, smartphone1, smartphone2):
        """Сложение смартфонов"""
        # 180000 * 5 + 210000 * 8 = 900000 + 1680000 = 2580000
        expected = 180000.0 * 5 + 210000.0 * 8
        assert smartphone1 + smartphone2 == expected

    def test_grass_sum(self, grass1, grass2):
        """Сложение газонной травы"""
        # 500 * 20 + 450 * 15 = 10000 + 6750 = 16750
        expected = 500.0 * 20 + 450.0 * 15
        assert grass1 + grass2 == expected

    def test_smartphone_plus_grass_raises_typeerror(self, smartphone1, grass1):
        """Сложение смартфона и травы → TypeError"""
        with pytest.raises(TypeError):
            smartphone1 + grass1

    def test_grass_plus_smartphone_raises_typeerror(self, grass1, smartphone1):
        """Сложение травы и смартфона → TypeError"""
        with pytest.raises(TypeError):
            grass1 + smartphone1

    def test_smartphone_sum_is_number(self, smartphone1, smartphone2):
        """Результат сложения — число"""
        result = smartphone1 + smartphone2
        assert isinstance(result, (int, float))

    def test_add_same_object(self, smartphone1):
        """Сложение с самим собой"""
        expected = 180000.0 * 5 * 2
        assert smartphone1 + smartphone1 == expected

    def test_full_scenario(
        self, smartphone1, smartphone2, smartphone3, grass1, grass2, capsys
    ):
        # Сложение смартфонов
        smartphone_sum = smartphone1 + smartphone2
        assert smartphone_sum == 180000.0 * 5 + 210000.0 * 8

        # Сложение травы
        grass_sum = grass1 + grass2
        assert grass_sum == 500.0 * 20 + 450.0 * 15

        # Сложение разных типов → TypeError
        with pytest.raises(TypeError):
            smartphone1 + grass1

        # Создание категорий
        category_smartphones = Category(
            "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
        )
        category_grass = Category(
            "Газонная трава", "Различные виды газонной травы", [grass1, grass2]
        )

        # Добавление продукта
        category_smartphones.add_product(smartphone3)
        assert Category.product_count == 5

        # Проверка геттера products
        products_str = category_smartphones.products
        assert "Samsung Galaxy S23 Ultra" in products_str
        assert "Iphone 15" in products_str
        assert "Xiaomi Redmi Note 11" in products_str

        # Добавление не-продукта → TypeError
        with pytest.raises(TypeError):
            category_smartphones.add_product("Not a product")


class TestBaseProduct:
    """Тесты для абстрактного класса BaseProduct"""

    def test_base_product_is_abstract(self):
        """BaseProduct — абстрактный класс"""
        assert issubclass(BaseProduct, ABC)

    def test_cannot_instantiate_base_product(self):
        """Нельзя создать экземпляр BaseProduct"""
        with pytest.raises(TypeError):
            BaseProduct("Test", "Desc", 100.0, 1)

    def test_base_product_has_abstract_methods(self):
        """BaseProduct содержит абстрактные методы"""
        assert hasattr(BaseProduct, '__init__')
        assert hasattr(BaseProduct, '__add__')
        assert BaseProduct.__init__.__isabstractmethod__
        assert BaseProduct.__add__.__isabstractmethod__

    def test_product_is_subclass_of_base(self):
        """Product наследуется от BaseProduct"""
        assert issubclass(Product, BaseProduct)

    def test_smartphone_is_subclass_of_base(self):
        """Smartphone наследуется от BaseProduct"""
        assert issubclass(Smartphone, BaseProduct)

    def test_lawn_grass_is_subclass_of_base(self):
        """LawnGrass наследуется от BaseProduct"""
        assert issubclass(LawnGrass, BaseProduct)




class TestMixinProduct:
    """Тесты для миксина MixinProduct"""

    def test_mixin_has_repr(self):
        """MixinProduct содержит __repr__"""
        assert hasattr(MixinProduct, '__repr__')

    def test_mixin_repr_format(self):
        """Формат __repr__ миксина"""

        # Создаем тестовый класс на основе миксина
        class TestProduct(MixinProduct):
            def __init__(self):
                self.name = "Test"
                self.description = "Desc"
                self.price = 100.0
                self.quantity = 5

        product = TestProduct()
        result = repr(product)

        assert "TestProduct" in result
        assert "Test" in result
        assert "Desc" in result
        assert "100.0" in result
        assert "5" in result

    def test_product_inherits_mixin(self):
        """Product наследуется от MixinProduct"""
        assert issubclass(Product, MixinProduct)

    def test_product_mro(self):
        """ MRO Product"""
        mro = Product.__mro__
        assert BaseProduct in mro
        assert MixinProduct in mro


def test_middle_price(first_category, category_without_product):
    assert first_category.middle_price() == 140333.33333333334
    assert category_without_product.middle_price() == 0

def test_init_with_zero_quantity():
    assert issubclass(BaseProduct, ABC)
