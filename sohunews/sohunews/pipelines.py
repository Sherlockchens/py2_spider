# -*- coding: utf-8 -*-
import codecs
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SohunewsPipeline(object):
    def __init__(self):
        self.file = codecs.open("mydata.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        # print item["name"]
        # print item["link"]
        # print "-"*20
        i = json.dumps(dict(item), ensure_ascii=False)
        line = i + '\n'
        print line
        self.file.write(line)
        return item
    def close_spider(self, spider):
        self.file.close()