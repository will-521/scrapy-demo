import scrapy
import logging
import json

log = logging.getLogger()

baseURL = 'http://www.danjuanfunds.com'


class DanjuanfundsSpider(scrapy.Spider):
    name = 'danjuanfunds'
    allowed_domains = ['www.danjuanfunds.com']
    page = 1

    def start_requests(self):
        for fundType in [1]:
            url = baseURL + '/djapi/v3/filter/fund?type=' + str(fundType) + '&order_by=1m&size=20&page=' + str(self.page)
            yield scrapy.Request(url=url, callback=self.parse, meta={"fundTypes": {"fundType": fundType}})

    def parse(self, response):
        fundType = response.meta['fundTypes']['fundType']
        body = json.loads(response.body)
        total_pages = body['data']['total_pages']
        log.info(total_pages)
        log.info(body)
        items = body['data']['items']
        for item in items:
            yield scrapy.Request(
                url=baseURL + '/djapi/fund/asset_conf?fd_code=' + str(item["fd_code"]),
                callback=self.parse_funds,
                meta={"item": item}
            )

        if self.page <= total_pages:
            self.page += 1
            yield scrapy.Request(
                url=baseURL + '/djapi/v3/filter/fund?type=' + str(fundType) + '&order_by=1m&size=1&page=' + str(
                    self.page),
                callback=self.parse,
                meta={"fundTypes": {"fundType": fundType}}
            )

    @staticmethod
    def parse_funds(response):
        item = response.meta["item"]
        body = json.loads(response.body)
        if 'data' in body:
            item['stack_list'] = body['data']['stock_list']
            yield item
