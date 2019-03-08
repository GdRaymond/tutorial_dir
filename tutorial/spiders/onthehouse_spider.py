# -*- coding: utf-8 -*-
import scrapy


class OnthehouseSpiderSpider(scrapy.Spider):
    name = 'onthehouse_spider'
    allowed_domains = ['https://www.onthehouse.com.au']
    start_urls = ['https://www.onthehouse.com.au/property/qld/oxley-4075/65-11-oakmont-ave-oxley-qld-4075-3712694?status=off-market,for-rent,for-sale&addressQuery=11%20Oakmont%20Ave,%20Oxley,%20QLD%204075']

#failed 2019 03 07 as the website rejected and failed to visit directly on splash info website

    def parse(self, response):
        pass
