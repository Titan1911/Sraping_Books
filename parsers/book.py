from locators.book_locators import BookLocator

class BookParser:

    RATINGS = {
        'One' : 1,
        'Tow' : 2,
        'Three' : 3,
        'Four' : 4,
        'Five' : 5
    }

    def __init__(self,parent):
        self.parent = parent

    def __repr__(self):
        return f'Book Name : {self.title}   Price : {self.price}    Rating : {self.rating} star rating'

    
    @property
    def title(self):
        locator = BookLocator.TITLE
        title_link = self.parent.select_one(locator)
        return title_link.attrs['title']

    @property
    def rating(self):
        locator = BookLocator.RATING
        rating_link = self.parent.select_one(locator)
        rating_attrs = rating_link.attrs['class']
        rating_final = [e for e in rating_attrs if e != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_final[0], 0)
        return rating_number

    @property
    def availability(self):
        locator = BookLocator.AVAILABILITY
        return self.parent.select_one(locator)

    @property
    def price(self):
        locator = BookLocator.PRICE
        price_link = self.parent.select_one(locator).string
        return float(price_link.strip('£'))

    @property
    def link(self):
        locator = BookLocator.LINK
        link_link = self.parent.select_one(locator)
        return link_link.attrs['href']
    

