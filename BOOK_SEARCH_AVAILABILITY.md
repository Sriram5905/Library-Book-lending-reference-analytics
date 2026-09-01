# BOOK_SEARCH_AVAILABILITY

## User Story
As a library user, I want to search and view the availability of a book so that I can decide whether to borrow or reserve it.

## Feature Description
This project provides a beginner-friendly library book search feature. A user can search for books by title, author, or ISBN and immediately view each matched book's availability status.

## Functional Requirements
- Search books by title, author, or ISBN.
- Display matching book details.
- Show current availability status as one of:
  - Available
  - Currently Borrowed
  - Reserved
- Show clear guidance to help the user decide whether to borrow now or reserve.

## Search Functionality
The `search_books` function performs case-insensitive matching against:
- `title`
- `author`
- `isbn` (exact match)

If the user enters an empty query, no results are returned.

## Book Availability Functionality
Each book has an `availability_status`. The `borrowing_guidance` function converts this status into a clear action for the user:
- **Available** → user can borrow now.
- **Currently Borrowed** or **Reserved** → user should place a reservation.

## Proposed User Workflow
1. User opens the app.
2. User enters a title, author, or ISBN.
3. App searches matching books.
4. App displays each match with details and availability status.
5. App displays guidance so user knows whether to borrow or reserve.

## Expected Benefits
- Helps users quickly check if a book is available.
- Reduces confusion around borrowing vs. reserving.
- Simple structure suitable for learning and GitHub workflow assignments.

## Future Improvements
- Connect to a persistent database.
- Add real-time borrow/reserve updates.
- Add filters by category, publication year, or language.
- Add a web interface for easier access.
