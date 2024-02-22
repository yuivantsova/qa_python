import pytest

from main import BooksCollector

class TestBooksCollector:
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_list_of_genre_true(self, collector):
        for genre in ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']:
            assert genre in collector.genre

    def test_list_of_genre_age_rating(self, collector):
        for genre_age_rating in ['Ужасы', 'Детективы']:
            assert genre_age_rating in collector.genre

    @pytest.mark.parametrize('name', ['Жареные зеленые помидоры в кафе "Полуста"',
                                      'Жареные зеленые помидоры в кафе "Полустан"'])
    def test_add_new_book_41_and_42_symbols(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('name', ['Жареные зеленые помидоры в кафе "Полуст"', 'G'])
    def test_add_new_book_39_and_1_symbols(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_0_symbols(self, collector):
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_number_in_title(self, collector):
        collector.add_new_book('1984')

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_title_latin(self, collector):
        collector.add_new_book('Dark Tower')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_same_books(self, collector):
        collector.add_new_book('Хоббит, туда и обратно')
        collector.add_new_book('Хоббит, туда и обратно')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['Хоббит, туда и обратно'])
    def test_add_new_book_no_genre(self, collector, new_book, name):

        assert collector.get_book_genre(name) == ''

    @pytest.mark.parametrize('name, genre, result',
    [
        ['Хоббит, туда и обратно', 'Фантастика', 'Фантастика'],
        ['Хоббит, туда и обратно', 'Фентази', ''],
    ])
    def test_set_book_genre_book_true(self, collector, new_book, name, genre, result):
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == result

    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Хоббит, туда и обратно', 'Фантастика'],
                                 ['Артур', 'Фентази']
                             ])
    def test_set_book_genre_book_false(self, collector, name, genre):
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == None

    def test_get_books_with_specific_genre_three_books(self, collector):
        collector.add_new_book('Молчание ягнят')
        collector.add_new_book('Сияние')
        collector.add_new_book('Чиполлино')

        collector.set_book_genre('Молчание ягнят', 'Ужасы')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('Чиполлино', 'Мультики')

        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_for_children_two_books_added(self, collector):
        collector.add_new_book('Незнайка')
        collector.add_new_book('Один дома')

        collector.set_book_genre('Незнайка', 'Мультфильмы')
        collector.set_book_genre('Один дома', 'Комедии')

        assert len(collector.get_books_for_children()) == 2

    def test_get_books_for_children_two_books_not_added(self, collector):
        collector.add_new_book('Сияние')

        collector.set_book_genre('Сияние', 'Ужасы')

        assert len(collector.get_books_for_children()) == 0

    @pytest.mark.parametrize('name_1, name_2, result',
                             [
                                 ['Незнайка', 'Сияние', 2]
                             ])
    def test_add_book_in_favorites_two_book_added(self, collector, name_1, name_2, result):
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)

        collector.add_book_in_favorites(name_1)
        collector.add_book_in_favorites(name_2)

        assert len(collector.get_list_of_favorites_books()) == result

    @pytest.mark.parametrize('name', ['Хоббит, туда и обратно'])
    def test_add_book_in_favorites_same_book_not_added(self, collector, new_book, name):

        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_book_not_book_genre(self, collector):
        collector.add_book_in_favorites('Незнайка')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_two_books_deleted(self, collector):

        collector.add_new_book('Незнайка')
        collector.add_new_book('Сияние')

        collector.add_book_in_favorites('Незнайка')
        collector.add_book_in_favorites('Сияние')

        collector.delete_book_from_favorites('Незнайка')
        collector.delete_book_from_favorites('Сияние')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_book_not_in_favorites(self, collector):

        collector.add_new_book('Незнайка')

        collector.delete_book_from_favorites('Незнайка')

        assert len(collector.get_list_of_favorites_books()) == 0








