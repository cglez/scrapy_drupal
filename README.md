## Overview

Scrapy bot to extract nodes and other data from Drupal sites.

It can be used to traverse a Drupal website and extract nodes
recreating the content types and fields structure. It can follow
links listed under taxonomy terms. It also provides a conversion
script to use the extracted data with node_export module import
feature.

## Requirements

* Python 2.7
* Scrapy 0.24

## Use
Set up the node types and fields you want to extract in items.py file.
Configure the websites to extract from, the taxonomy terms to use, etc. in
spiders/example.py file. Follow the provided examples.

Then browse to the scrapy_drupal root folder and run:
```
scrapy crawl example -o data.json
```

## Copyright

Copyright (c) 2014 Cesar Gonzalez

This program is distributed under the General Public License version 3,
see the LICENSE file for more details.

