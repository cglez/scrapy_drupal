# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


# Here we can define general items or more specific ones targeting
# content types in particular, in this case we recreate the content
# type structure by defining its specific fields

# Content type item template
class ScrapyDrupalContentType(Item):
    # general node information
    url = Field()
    title = Field()
    pubdate = Field()
    author = Field()

    # taxonomy
    vocabulary1 = Field()
    vocabulary2 = Field()

    # main node content
    summary = Field()
    body = Field()

    # specific drupal fields
    field_name1 = Field()
    field_name2 = Field()


# Example general item with common information and some specific fields
class ScrapyDrupalNode(Item):
    # define the fields for your item here like:
    # name = Field()

    # general information
    url = Field()
    title = Field()
    pubdate = Field()
    author = Field()

    # taxonomy
    tags = Field()

    # main content
    summary = Field()
    body = Field()

    # specific fields
    picture = Field()
    picture_url = Field()
    figcaption = Field()
    smallpic = Field()
