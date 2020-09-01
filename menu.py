from app import books_list

def print_best_books(): #5 rating books
    best_books = sorted(books_list, key=lambda x: x.rating, reverse=True)
    for book in best_books:
        if book.rating == 5:
            print(book)

print_best_books()