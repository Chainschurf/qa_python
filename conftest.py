import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def add_book(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')