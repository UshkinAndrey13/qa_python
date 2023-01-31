import pytest
from main import BooksCollector


@pytest.fixture
def books_collector():
    collector = BooksCollector()
    collector.add_new_book('Трудно быть богом')
    collector.add_new_book('Пикник на обочине')
    return collector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2


    def test_add_new_book_twice(self):

        collector = BooksCollector()

        collector.add_new_book('Трудно быть богом')
        collector.add_new_book('Трудно быть богом')

        assert collector.books_rating == {'Трудно быть богом': 1}



    def test_add_rating_to_absent_book_fails(self):

        collector = BooksCollector()

        collector.add_new_book('Трудно быть богом')
        collector.set_book_rating('Пикник на обочине', 5)

        assert collector.books_rating == {'Трудно быть богом': 1}



    def test_set_rating_less_than_one_fails(self):

        collector = BooksCollector()

        collector.add_new_book('Трудно быть богом')
        collector.set_book_rating('Трудно быть богом', 0)

        assert collector.books_rating == {'Трудно быть богом': 1}



    def test_set_rating_higher_than_ten_fails(self):

        collector = BooksCollector()

        collector.add_new_book('Трудно быть богом')
        collector.set_book_rating('Трудно быть богом', 11)

        assert collector.books_rating == {'Трудно быть богом': 1}



    def test_absent_book_has_no_rating(self):

        collector = BooksCollector()

        collector.add_new_book('Трудно быть богом')
        rating = collector.get_book_rating('Пикник на обочине')

        assert rating is None



    def test_add_to_favorites(self, books_collector):

        books_collector.add_new_book('Трудно быть богом')
        books_collector.add_book_in_favorites('Трудно быть богом')

        assert books_collector.favorites == ['Трудно быть богом']



    def test_add_to_favorites_if_not_in_ratings_fails(self):

        collector = BooksCollector()

        collector.add_book_in_favorites('Трудно быть богом')

        assert collector.favorites == []
        assert collector.books_rating == {}


    def test_delete_from_favorites(self, books_collector):

        books_collector.add_new_book('Трудно быть богом')
        books_collector.add_book_in_favorites('Трудно быть богом')
        books_collector.delete_book_from_favorites('Трудно быть богом')

        assert books_collector.favorites == []



    def test_get_list_of_favorites_books(self, books_collector):
        books_collector.add_new_book('Трудно быть богом')
        books_collector.add_book_in_favorites('Трудно быть богом')

        assert books_collector.get_list_of_favorites_books() == ['Трудно быть богом']