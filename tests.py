import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('book', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_add_two_books(self, collector, book):
        collector.add_new_book(book[0])
        collector.add_new_book(book[1])

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book', ['Lorem ipsum dolor sit amet, consectetur adipiscing elit'])
    def test_add_new_book_add_too_long_name(self, collector, book):
        collector.add_new_book(book)

        assert book not in collector.books_genre

    @pytest.mark.parametrize('book, genre', [['Гордость и предубеждение и зомби', 'Фантастика']])
    def test_set_book_genre_add_new_genre(self, collector, add_book, book, genre):
        collector.set_book_genre(book, genre)

        assert collector.books_genre.get(book) == genre

    @pytest.mark.parametrize('book', ['Гордость и предубеждение и зомби'])
    def test_get_book_genre_new_book_has_no_genre(self, collector, add_book, book):

        assert collector.books_genre.get(book) == ''

    @pytest.mark.parametrize('book, genre', [['Гордость и предубеждение и зомби', 'Фантастика']])
    def test_get_book_genre_new_book_has_genre(self, collector, add_book, book, genre):
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == collector.books_genre.get(book)

    @pytest.mark.parametrize('book, genre', [['Гордость и предубеждение и зомби', 'Фантастика']])
    def test_get_books_with_specific_genre_request_genre(self, collector, add_book, book, genre):
        collector.set_book_genre(book, genre)

        assert book in collector.get_books_with_specific_genre(genre)

    @pytest.mark.parametrize('book, genre', [['Гордость и предубеждение и зомби', 'Фантастика']])
    def test_get_books_genre_returns_book_and_genre(self, collector, add_book, book, genre):
        collector.set_book_genre(book, genre)

        assert collector.get_books_genre() == collector.books_genre

    @pytest.mark.parametrize('book, genre', [['Гордость и предубеждение и зомби', 'Ужасы']])
    def test_get_books_for_children_no_adult_books_in_result(self, collector, add_book, book, genre):
        collector.set_book_genre(book, genre)

        assert collector.get_books_for_children() == []

    @pytest.mark.parametrize('book', ['Гордость и предубеждение и зомби'])
    def test_add_book_in_favorites_no_duplicates(self, collector, add_book, book):
        collector.add_book_in_favorites(book)
        collector.add_book_in_favorites(book)

        assert len(collector.favorites) == 1

    @pytest.mark.parametrize('book', ['Гордость и предубеждение и зомби'])
    def test_delete_book_from_favorites_book_is_deleted(self, collector, add_book, book):
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)

        assert collector.favorites == []

    @pytest.mark.parametrize('book', ['Гордость и предубеждение и зомби'])
    def test_get_list_of_favorites_books_list_not_empty(self, collector, add_book, book):
        collector.add_book_in_favorites(book)

        assert book in collector.favorites
