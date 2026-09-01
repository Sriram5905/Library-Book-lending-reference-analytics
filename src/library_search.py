from dataclasses import dataclass
from typing import List


AVAILABLE = "Available"
BORROWED = "Currently Borrowed"
RESERVED = "Reserved"


@dataclass
class Book:
    title: str
    author: str
    isbn: str
    availability_status: str


def get_sample_books() -> List[Book]:
    return [
        Book("The Pragmatic Programmer", "Andrew Hunt", "9780201616224", AVAILABLE),
        Book("Clean Code", "Robert C. Martin", "9780132350884", BORROWED),
        Book("Design Patterns", "Erich Gamma", "9780201633610", RESERVED),
    ]


def search_books(books: List[Book], query: str) -> List[Book]:
    normalized_query = query.strip().lower()
    if not normalized_query:
        return []

    return [
        book
        for book in books
        if normalized_query in book.title.lower()
        or normalized_query in book.author.lower()
        or normalized_query == book.isbn.lower()
    ]


def borrowing_guidance(status: str) -> str:
    if status == AVAILABLE:
        return "You can borrow this book now."
    if status in {BORROWED, RESERVED}:
        return "This book is not available right now. You should place a reservation."
    return "Status unavailable. Please ask the librarian for help."


def format_book_result(book: Book) -> str:
    return (
        f"Title: {book.title}\n"
        f"Author: {book.author}\n"
        f"ISBN: {book.isbn}\n"
        f"Availability: {book.availability_status}\n"
        f"Action: {borrowing_guidance(book.availability_status)}"
    )
