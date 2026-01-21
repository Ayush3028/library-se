import unittest
from src.library import Library


class TestLibrary(unittest.TestCase):

    def test_add_book_success(self):
        lib = Library()
        lib.add_book(1, "Python", "Guido")
        self.assertIn(1, lib.books)

    def test_add_duplicate_book(self):
        lib = Library()
        lib.add_book(1, "Python", "Guido")
        with self.assertRaises(ValueError):
            lib.add_book(1, "Java", "James")

    def test_borrow_book(self):
        lib = Library()
        lib.add_book(1, "Python", "Guido")
        lib.borrow_book(1)
        self.assertEqual(lib.books[1]["status"], "Borrowed")

    def test_borrow_unavailable_book(self):
        lib = Library()
        lib.add_book(1, "Python", "Guido")
        lib.borrow_book(1)
        with self.assertRaises(ValueError):
            lib.borrow_book(1)


if __name__ == "__main__":
    unittest.main()

