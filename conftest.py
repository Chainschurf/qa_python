import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def add_book(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')


@pytest.fixture
def set_genre(collector):
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')


@pytest.fixture
def favorites_add(collector):
    collector.add_book_in_favorites('Гордость и предубеждение и зомби')