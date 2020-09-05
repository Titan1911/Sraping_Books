import requests

from pages.book_page import BookPage


page_content = requests.get('http://books.toscrape.com/').content
page = BookPage(page_content)
books_list = page.books

"""
for page_num in range(2, page.page_count):
    page_content = requests.get(f'http://books.toscrape.com/catalogue/page-{page_num}.html').content
    page = BookPage(page_content)

    books_list.extend(page.books)
"""

for books in books_list:
    print(books) #default __repr__ function


