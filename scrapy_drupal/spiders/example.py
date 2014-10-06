# -*- coding: utf-8 -*-

# This spider bot extracts information from a drupal site, starting from
# a taxonomy term, traverses the paginator and gets the elements of all
# nodes under that category

# For this bot we are using the CrawlSpider with some Rules
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from scrapy_drupal.items import ScrapyDrupalNode


class ExampleSpider(CrawlSpider):
    name = "example"
    allowed_domains = ["example.com"]

    # use a taxonomy term as a start point regardless whether the site
    # is using pretty urls or not
    start_urls = (
        'http://www.example.com/?q=taxonomy/term/1',
    )

    rules = (
        # first traverse all the pages in the paginator
        Rule(LinkExtractor(allow=('page=\d+', ))),
        # extract the information in the elements that end with '.html'
        Rule(LinkExtractor(allow=['\.html']), callback='parse_node'),
    )

    def parse_node(self, response):
        node = ScrapyDrupalItem()
        # extract the url
        node['url'] = response.url
        # assume title is wrapped in a h1 element
        node['title'] = response.xpath("//header/hgroup/h1//text()").extract()
        # publication date is under a time tag
        node['pubdate'] = response.xpath("//time/text()").extract()
        # author links has rel='author' attribute
        node['author'] = response.xpath("//a[@rel='author']/text()").extract()

        # tag links are under an unshorted list with class 'tags'
        node['tags'] = response.xpath("//ul[@class='tags']/li/a/text()").extract()

        # summary is wrapped in a h2 element
        node['summary'] = response.xpath("//header/hgroup/h2//text()").extract()
        # body content is under a div with class 'entry', here we extract everything
        node['body'] = response.xpath("//div[@class='entry']/node()").extract()

        # other fields
        node['picture_url'] = response.xpath("//header//figure/img/@src").extract()
        node['figcaption'] = response.xpath("//header//figcaption/node()").extract()

        return node
