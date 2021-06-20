from multiprocessing import Process
from scrapy import cmdline
import time
import logging

confs = [
    {
        "spider_name": "xueqiuindexspider",
        "frequency": 2,
    },
    {
        "spider_name": "xueqiuspider",
        "frequency": 3,
    },

]


def start_spider(spider_name, frequency):
    args = ["scrapy", "crawl", spider_name]
    while True:
        start = time.time()
        p = Process(target=cmdline.execute, args=(args,))
        p.start()
        p.join()
        logging.debug("### use time: %s" % (time.time() - start))
        time.sleep(frequency)


if __name__ == '__main__':
    for conf in confs:
        process = Process(target=start_spider, args=(conf["spider_name"], conf["frequency"]))
        process.start()
        waitTime = 60 * 10
        logging.debug('I will sleep a moment, thanks')
        time.sleep(waitTime)
