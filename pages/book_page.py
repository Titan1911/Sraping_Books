from bs4 import BeautifulSoup
from parsers.book import BookParser
from locators.book_page_locators import BookPageLocator

class BookPage:
    def __init__(self,page):
        self.soup = BeautifulSoup(page, 'html.parser')
        
    @property
    def books(self):
        locator = BookPageLocator.BOOK
        book_link = self.soup.select(locator)
        return [BookParser(e) for e in book_link]
