import scrapy
import logging
import json
log = logging.getLogger()


class XueqiuindexspiderSpider(scrapy.Spider):
    name = 'xueqiuindexspider'
    allowed_domains = ['xueqiu.com']
    start_urls = ['https://xueqiu.com/service/v5/stock/batch/quote?symbol=SH000001,SZ399001,SZ399006,SH000688']

    def parse(self, response):
        body = json.loads(response.body)
        log.info(body)
        for item in body['data']['items']:
            item['spiderType'] = 'quoteIndex'
            yield item
