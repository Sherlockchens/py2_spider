# -*- coding: utf-8 -*-
import scrapy
from baike.items import BaikeItem
from urlparse import urljoin
import urllib2

class BaikespdSpider(scrapy.Spider):
    name = "baikespd"
    allowed_domains = ["baidu.com"]
    keyword = "能源"
    # start_urls = ['http://baike.baidu.com/search?word=%E5%AE%89%E5%BE%BD&pn=0&rn=0&enc=utf8',]
    start_urls = ['http://baike.baidu.com/search?word={}&pn=0&rn=0&enc=utf8'.format(keyword)]
    
    def __init__(self, search=None, *args, **kwargs):
        super(BaikespdSpider, self).__init__(*args, **kwargs)
        if search is not None:
            word = urllib2.quote(search.decode("gbk").encode("utf-8"))
            myurl = 'http://baike.baidu.com/search?word={}&pn=0&rn=0&enc=utf8'.format(word)
            # myurl = urllib.quote(url)
            # myurl = urllib.unquote(url2)
            self.start_urls.append(myurl)
    def parse(self, response):
        urls = response.xpath("//a[@class='result-title']/@href").extract()
        for urltail in urls:
            url = urljoin("http://baike.baidu.com",urltail)
            yield scrapy.Request(url, callback=self.item_parse)
    def item_parse(self, response):
        items = BaikeItem()
        items["link"] = response.url
        items["title"] = response.xpath("/html/head/title/text()").extract()
        items["content"] = response.xpath("//meta[@name='description']/@content").extract()
        return items
