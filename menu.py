from app import books_list

def best_books(): #5 rating books
    best_books = sorted(books_list, key=lambda x: x.rating, reverse=True)
    for book in best_books:
        if book.rating == 5 or book.rating == 4: #or for finding top 10(any number) books then list slicing on best_books line for eg. [:10]
            print(book)

def cheapest_books():
    cheapest_books = sorted(books_list, key=lambda x: x.price, reverse=False)[:10]
    for book in cheapest_books:
        print(book)

def best_cheap_books():
    best_cheap_books = sorted(books_list, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_cheap_books:
        print(book)

'''
#useful while making a user menu.
def get_next_book():
    print(next(x for x in books_list)) #this next is a generator
'''
# print_best_books()
# cheapest_books()
best_cheap_books()
# get_next_book()