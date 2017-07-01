# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy import signals
from scrapy.exceptions import DropItem
from scrapy.exporters import XmlItemExporter
from scrapy.exporters import CsvItemExporter

class JDselfsalePipeline(object):
	# def __init__(self):  
 #        self.ids_seen = set() 
    def open_spider(self, JDspider):
    	self.file1= open('JD_items.jl', 'a')
    	self.file2=open('JD_items.json','a')
    	self.file2.write('[\n')
    def process_item(self,jd_item,JDspider):  
        # if not jd_item['flag']:  
        #     raise DropItem("item dropped found: %s" % jd_item)  
        # else:
    	str_line1= json.dumps(dict(jd_item)) + "\n"
    	self.file1.write(str_line1)
    	str_line2=json.dumps(dict(jd_item))+','+'\n'
    	self.file2.write(str_line2)

    	return jd_item
    def close_spider(self, JDspider):
    	self.file1.close()
    	self.file2.write(']')
    	self.file2.close()   
            # self.ids_seen.add(item['id'])  
             


# class XmlExportPipeline(object):
# 	def __init__(self): 
# 		dispatcher.connect(self.spider_opened, signals.spider_opened)
# 		dispatcher.connect(self.spider_closed, signals.spider_closed)
# 		self.files = {}
# 		# self.file = open('product.csv' , 'w') 
		
# 		# self.exporter=CsvItemExporter(file)

# 		# self.exporters = {}


# 	# @classmethod
# 	# def from_crawler(cls, crawler):
# 	# 	pipeline = cls()
# 	# 	crawler.
		
# 	# 	return pipeline
# 	def spider_opened(self,JDspider):
# 		file=open('%s_products.xml'% JDspisdr.name,'wb')
# 		self.files[JDspider]=self.file
# 		self.exporter.start_exporting()
# 	def spider_closed(self, JDspider):
# 		self.exporter.finish_exporting()
# 		file = self.files.pop(JDspider) 
# 		file.close()
# 	def process_item(self, jd_item, JDspider):
# 		self.exporter.export_item(jd_item)
# 		return jd_item
	 


 
        
     






  
 



	 

  

    


    # def process_item(self, item, spider):
    	





    #     return item
