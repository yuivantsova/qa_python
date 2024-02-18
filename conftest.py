import pytest
from main import BooksCollector

@pytest.fixture
def list_genre():
    list_genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    return list_genre

@pytest.fixture
def list_genre_age_rating():
    list_genre_age_rating = ['Ужасы', 'Детективы']
    return list_genre_age_rating

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def new_book(collector):
    book = collector.add_new_book('Хоббит, туда и обратно')
    return book