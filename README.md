# Library Book Lending Reference Analytics

A simple beginner-friendly project that demonstrates book search and availability lookup for a library use case.

## User Story
As a library user, I want to search and view the availability of a book so that I can decide whether to borrow or reserve it.

## Project Structure
- `src/library_search.py` - Core data model and search/availability logic.
- `src/main.py` - Simple CLI flow for searching and viewing results.
- `tests/test_library_search.py` - Focused unit tests for search and availability behavior.
- `BOOK_SEARCH_AVAILABILITY.md` - Feature documentation.

## What the feature supports
- Search by title, author, or ISBN.
- View matching book details.
- View clear availability status:
  - Available
  - Currently Borrowed
  - Reserved
- Understand whether to borrow now or reserve.

## Run the app
From the repository root:

```bash
python src/main.py
```

## Run tests
From the repository root:

```bash
python -m unittest discover -s tests
```
