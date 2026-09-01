from library_search import format_book_result, get_sample_books, search_books


def run() -> None:
    books = get_sample_books()
    query = input("Search by title, author, or ISBN: ")

    matches = search_books(books, query)
    if not matches:
        print("No matching books found.")
        return

    for index, book in enumerate(matches, start=1):
        print(f"\nMatch {index}")
        print("-" * 30)
        print(format_book_result(book))


if __name__ == "__main__":
    run()
