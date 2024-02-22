# qa_python

1. ***test_list_of_genre_true*** - checking available genres
2. ***test_list_of_genre_age_rating*** - checking genre age rating
3. ***test_add_new_book_41_and_42_symbols*** - checking the title of a book with 41-symbols and 42-symbols 
4. ***test_add_new_book_39_and_1_symbols*** - checking the title of a book with 39-symbols and 1 symbol
5. ***test_add_new_book_0_symbols*** - checking the title of a book with a 0 symbol
6. ***test_add_new_book_title_latin*** - checking the title of a book with a Latin title
6. ***test_add_new_book_number_in_title*** - checking the title of a book with a number title
7. ***test_add_new_book_same_books*** - checking the add of identical books
8. ***test_add_new_book_no_genre*** - the added book has no genre
9. ***test_set_book_genre_book_true*** - the book is in books_genre. The parameterization includes data: the genre is in the genre list and the genre is not in the list.
11. ***test_set_book_genre_book_false*** - the book if the book is **not** in books_genre. The parameterization includes data: the genre is in the genre list and the genre is not in the list. 
14. ***test_get_books_with_specific_genre_three_books*** - checking the display of a list of books with a specific genre. 
1. ***test_get_books_for_children_two_books_added*** - checking the return of books whose genres are not included in the age limit list.
1. ***test_get_books_for_children_two_books_not_added*** - genres of books with an age rating will not be included in the list for children.
1. ***test_add_book_in_favorites_two_book_added*** - checking the addition of books to the favorites list.
1. ***test_add_book_in_favorites_same_book_not_added*** - checking that it is impossible to add two identical books
1. ***test_add_book_in_favorites_book_not_book_genre*** - checking that the list will remain empty if the book is not in book_genre.
1. ***test_delete_book_from_favorites_two_books_deleted*** - checking the removal of books from the favorites list.
1. ***test_delete_book_from_favorites_book_not_in_favorites*** - checking that a book that is in book_genre and is not in the favorites list will not be deleted from the book_genre list.
