from src.category import Category
from src.product import Product
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
