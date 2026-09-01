import unittest

from src.library_search import (
    AVAILABLE,
    BORROWED,
    RESERVED,
    borrowing_guidance,
    get_sample_books,
    search_books,
)


class TestLibrarySearch(unittest.TestCase):
    def setUp(self) -> None:
        self.books = get_sample_books()

    def test_search_by_title(self) -> None:
        results = search_books(self.books, "clean code")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Clean Code")

    def test_search_by_author(self) -> None:
        results = search_books(self.books, "andrew hunt")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "Andrew Hunt")

    def test_search_by_isbn(self) -> None:
        results = search_books(self.books, "9780201633610")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].availability_status, RESERVED)

    def test_empty_query_returns_no_results(self) -> None:
        self.assertEqual(search_books(self.books, "   "), [])

    def test_borrowing_guidance(self) -> None:
        self.assertIn("borrow", borrowing_guidance(AVAILABLE).lower())
        self.assertIn("reservation", borrowing_guidance(BORROWED).lower())


if __name__ == "__main__":
    unittest.main()
