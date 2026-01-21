import unittest
from src.library import Library

class TestLibrarySprint1(unittest.TestCase):

    def test_add_book_success(self):
        lib = Library()
        lib.add_book(1, "Python", "Guido")
        self.assertIn(1, lib.books)

    def test_add_duplicate_book(self):
        lib = Library()
        lib.add_book(1, "Python", "Guido")
        with self.assertRaises(ValueError):
            lib.add_book(1, "Java", "James")

if __name__ == "__main__":
    unittest.main()
