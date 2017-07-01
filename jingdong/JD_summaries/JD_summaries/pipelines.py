# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class JDSummariesPipeline(object):

    def open_spider(self, spider):
    	self.file1=open('JD_summaries.jl', 'a')
    	self.file2=open('JD_isummaries.json','a')
    	self.file2.write('[\n')
    def process_item(self,item,spider):  

    	str_line1=json.dumps(dict(item)) + "\n"
    	self.file1.write(str_line1)
    	str_line2=json.dumps(dict(item))+','+'\n'
    	self.file2.write(str_line2)

    	return item
    def close_spider(self,spider):
    	self.file1.close()
    	self.file2.write(']')
    	self.file2.close() 