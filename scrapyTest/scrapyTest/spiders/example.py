# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['exaple.com']
    start_urls = ['http://exaple.com/']

    def parse(self, response):
        pass
