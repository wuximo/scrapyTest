# -*- coding: utf-8 -*-
import scrapy

import re
from scrapyTest.items import scrapyTestItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        html = response.text
