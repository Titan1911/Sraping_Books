from bs4 import BeautifulSoup
import re

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

    @property
    def page_count(self):
        locator = BookPageLocator.PAGER
        page_count_link = self.soup.select_one(locator).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, page_count_link)
        return int(matcher.group(1))