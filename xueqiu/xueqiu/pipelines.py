# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from kafka import KafkaProducer
import json, logging
log = logging.getLogger()

class XueqiuPipeline:
    def process_item(self, data, spider):
        log.debug("--------------------start-------------------------")
        producer = KafkaProducer(bootstrap_servers='localhost:9092')  # 连接kafka
        print('quote result:', data['spiderType'])
        for item in data['list']:
            msg = json.dumps(item)
            # print('msg:', msg)
            print(data['spiderType'] +'2222222222')
            result = producer.send(data['spiderType'], msg.encode(), partition=0).get(timeout=60)
            print('quote result:', data['spiderType'], result)
        producer.close()
        log.debug("--------------------end-------------------------")
        return data

