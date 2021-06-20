# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import time
import logging
import json
# from kafka import KafkaProducer
from elasticsearch import Elasticsearch
import uuid

log = logging.getLogger()
es = Elasticsearch(
    [
        {"host": "localhost", "port": 9200}
    ],
    timeout=3600
)


class DanjuanfundscrawlPipeline:
    @staticmethod
    def process_item(item, spider):
        log.debug("--------------------start-------------------------")
        uid = str(uuid.uuid4())
        suid = ''.join(uid.split('-'))
        item['id'] = suid
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        item['createTime'] = now
        item['updateTime'] = now
        result = json.dumps(item)
        es.index('test_index',  result, id=suid)
        log.debug("--------------------end-------------------------")
        pass
