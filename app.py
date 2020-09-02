import requests

from pages.book_page import BookPage

page_content = requests.get('http://books.toscrape.com/').content
page = BookPage(page_content)
books_list = page.books


for n in range(2,51):
    page_content = requests.get(f'http://books.toscrape.com/catalogue/page-{n}.html').content
    page = BookPage(page_content)

    books_list.extend(page.books)

'''
for books in books_list:
    print(books) #default __repr__ function
    print(books.link)
'''
