import scrapy
import logging
import json
log = logging.getLogger()

class XueqiuSpider(scrapy.Spider):
    name = 'xueqiuspider'
    allowed_domains = ['xueqiu.com']
    start_urls = ['http://xueqiu.com/service/v5/stock/batch/quote?symbol=SH000001']

    def parse(self, response):
        body = json.loads(response.body)
        log.info(body)
        for item in body['data']['items']:
            item['spiderType'] = 'quoteIndex'
            yield item
