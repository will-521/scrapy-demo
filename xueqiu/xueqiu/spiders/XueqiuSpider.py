import scrapy, logging, json, random, time
log = logging.getLogger()

class XueqiuSpider(scrapy.Spider):
    name = 'xueqiuSpider'
    # start_urls = [
    #     # 'https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=30&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz'
    # ]

    def start_requests(self):
        req = 'https://xueqiu.com/service/v5/stock/screener/quote/list?page={}&size=30&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz'
        for i in range(1, 150):
            sleepTime = random.randint(1,5)
            log.debug(sleepTime)
            time.sleep(sleepTime)
            log.debug(req.format(str(i)))
            yield scrapy.Request(req.format(str(i)), callback=self.parse)

    def parse(self, response):
        body = json.loads(response.body)
        sleepTime = random.randint(1,3)
        log.info('--1--{}'.format(str(sleepTime)))
        time.sleep(sleepTime)
        if(body['error_code'] == 0):
            data = body['data']
            data['spiderType'] = 'quote'
            yield data


        



