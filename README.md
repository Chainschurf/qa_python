# qa_python Sprint_4

1. test_add_new_book_add_two_books:
Добавляет две книги, проверяет длину списка books_genre после добавления

2. test_add_new_book_add_too_long_name:
Добавляет книгу с названием длиннее 41 символа, проверяет, что книга не добавилась в список books_genre

3. test_set_book_genre_add_new_genre:
Проверяет, что при назначении жанра книге, этот жанр книге назначается

4. test_get_book_genre_new_book_has_no_genre:
Проверяет, что при добавлении новой книги у неё нет жанра

5. test_get_book_genre_new_book_has_genre:
Проверяет, что если жанр для книги добавлен, то при запросе get_book_genre показывается добавленный жанр

6. test_get_books_with_specific_genre_request_genre:
Проверяет, что при запросе жанра показываются относящиеся к этому жанру книги

7. test_get_books_genre_dict_not_empty:
Проверяет, что если добавить жанр, то при запросе жанра возвращается не пустой словарь

8. test_get_books_for_children_no_adult_books_in_result:
Проверяет, что если в books_genre добавлены только не подходяшие для детей жанры, то при запросе книг для детей возвращается пустой список

9. test_add_book_in_favorites_no_duplicates:
Проверяет, что если добавить в избранные две одинаковых книги, то в список favorites добавится только одна книга

10. test_delete_book_from_favorites_book_is_deleted:
Проверяет, что добавленная книга успешно удаляется из списка

11. test_get_list_of_favorites_books_list_not_empty:
Проверяет, что если добавить книгу в избранное, то при запросе избранного эта книга будет в списке