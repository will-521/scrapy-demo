# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from kafka import KafkaProducer
import json

class XueqiuindexPipeline:
    def process_item(self, item, spider):
        # producer = KafkaProducer(bootstrap_servers='localhost:9092')  # 连接kafka
        # msg = json.dumps(item)
        # print('msg:', msg)
        # result = producer.send(item['spiderType'], msg.encode(), partition=0).get(timeout=60)
        # print('quoteIndex result:', item['spiderType'], result)
        # producer.close()
        print("222222====!!!!!!")
        print(item)
        print("5555555")
        return item
