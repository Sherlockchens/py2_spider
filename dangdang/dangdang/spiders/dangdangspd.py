# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request

class DangdangspdSpider(scrapy.Spider):
    name = "dangdangspd"
    allowed_domains = ["dangdang.com"]
    start_urls = ['http://category.dangdang.com/pg1-cid4009587.html']

    def parse(self, response):
		item = DangdangItem()
		item["name"] = response.xpath("//a[@class='pic']/@title").extract()
		item["price"] = response.xpath("//span[@class='price_n']/text()").extract()
		item["link"] = response.xpath("//a[@class='pic']/@href").extract()
		item["comnum"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
		yield item
		for i in range(1,50):
			url = "http://category.dangdang.com/pg{}-cid4009587.html".format(i)
			yield Request(url, callback = self.parse)