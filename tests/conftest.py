from src.category import Category
from src.product import Product,Smartphone,LawnGrass
import pytest
from typing import List

@pytest.fixture
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_product() -> Product:
    """Фикстура: один тестовый продукт"""
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )


@pytest.fixture
def sample_products() -> List[Product]:
    """Фикстура: список тестовых продуктов"""
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


@pytest.fixture
def sample_category(sample_products) -> Category:
    """Фикстура: категория с продуктами"""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        sample_products
    )


@pytest.fixture
def reset_counters():
    """Фикстура: сбрасывает счетчики Category перед тестом"""
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products(product1, product2, product3) -> List[Product]:
    """Фикстура: список трёх продуктов"""
    return [product1, product2, product3]


@pytest.fixture
def product1() -> Product:
    """Фикстура: Samsung Galaxy S23 Ultra"""
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )


@pytest.fixture
def product2() -> Product:
    """Фикстура: Iphone 15"""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product3() -> Product:
    """Фикстура: Xiaomi Redmi Note 11"""
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

@pytest.fixture
def smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,"S23 Ultra", 256, "Серый")

@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

@pytest.fixture
def smartphone3():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

@pytest.fixture
def category_smartphones():
    return Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])

@pytest.fixture
def category_grass():
    return Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации",
        products=[
            Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),],)

@pytest.fixture
def category_without_product():
    return Category(
        name="Машины",
        description="Современный автомобиль, который позволяет наслаждаться вождением",
        products=[]
    )
