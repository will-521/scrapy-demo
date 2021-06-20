import json
import logging

import scrapy

log = logging.getLogger()
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class XueqiuindexspiderSpider(scrapy.Spider):
    name = 'xueqiuindexspider'
    allowed_domains = ['xueqiu.com']
    start_urls = ['https://xueqiu.com/service/v5/stock/batch/quote?symbol=SZ399006,SH000688']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow='/service/v5/stock/batch/quote?symbol=SZ399006,SH000688')),
    )

    def parse(self, response):
        body = json.loads(response.body)
        log.info(body)
        for item in body['data']['items']:
            item['spiderType'] = 'quoteIndex'
            yield item
