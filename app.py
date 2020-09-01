import requests

from pages.book_page import BookPage

page_content = requests.get('http://books.toscrape.com/').content
page = BookPage(page_content)

books_list = page.books
