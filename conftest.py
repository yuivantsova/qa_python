import pytest
from main import BooksCollector


@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture(scope='function')
def new_book(collector):
    book = collector.add_new_book('Хоббит, туда и обратно')
    return book