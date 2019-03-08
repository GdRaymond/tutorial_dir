import scrapy
from scrapy.spiders import Spider
from scrapy_splash import SplashRequest
from scrapy import Request
from tutorial.spiders.user_agent import get_user_agent

class SplashTestSpider(Spider):
    name='splash_test'
    #start_urls=['https://item.jd.com/7321794.html']
    start_urls=['https://item.jd.com/7321794.html']

    def start_requests(self):
        for url in self.start_urls:
            my_header={
                'referer':'https://item.jd.com/7321794.html',
                'user-agent':get_user_agent(),
            }
            #yield SplashRequest(url=url,callback=self.parse,args={'wait':0.5,'time_out':90})
            yield  Request(url,self.parse)

    def parse(self,response):
        bd=response.css('body::text').extract()
        print('body={0}'.format(bd))
        prices=response.xpath('//*[@class="p-price"]/span/text()').extract()
        print('price={0}'.format(prices[1]))
