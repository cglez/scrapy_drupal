# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_drupal project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_drupal'

SPIDER_MODULES = ['scrapy_drupal.spiders']
NEWSPIDER_MODULE = 'scrapy_drupal.spiders'
DEFAULT_ITEM_CLASS = 'scrapy_drupal.items.ScrapyDrupalItem'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_drupal (+http://www.yourdomain.com)'
