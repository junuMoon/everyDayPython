from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime

def remove_quotes(text):
    """ strip the unicode quotes """
    text = text.strip(u'\u201c')
    text = text.strip(u'\u201d')
    return text


def convert_date(date_text):
    """ convert string March 14 to datetime object """
    return datetime.strptime(date_text, "%B %d, %Y" )


def parse_location(location_text):
    """ 
    parse location in Born information
    This simply remove "in" in string.
    You can further parse city, state, country, etc.
    """
    return location_text[3:]
    

class QuoteItem(Item):
    quote_content = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )
    author_name = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    author_birthdate = Field(
        input_processor=MapCompose(convert_date),
        output_processor=TakeFirst()
    )
    author_bornlocation = Field(
        input_processor=MapCompose(parse_location),
        output_processor=TakeFirst()
    )
    author_bio = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    tags = Field()