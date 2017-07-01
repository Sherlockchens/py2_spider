#coding=utf-8
'''
Created on Mar 26, 2017

@author: fate
'''
import re
import scrapy
import json
#from myproject.items import MyprojectItem
from scrapy_splash import SplashRequest
class  MySpider(scrapy.Spider):
    name='splash'
    def start_requests(self):
        start_urls=[
        'https://item.jd.com/1760146.html',
        'http://item.jd.com/11545298993.html',
        'http://item.jd.com/1451400.html',
        'http://item.jd.com/1069486.html',
        'http://item.jd.com/10029157646.html',]
        for url in start_urls:
            yield SplashRequest(url,callback=self.parse,args={'wait':0.5})
            
        #http://club.jd.com/ProductPageService.aspx?method=GetCommentSummaryBySkuId&referenceId=1760146
        
    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
       # item=MyprojectItem()
        price=response.xpath('//span[@class="p-price"]/span[@class]/text()').extract_first() 
        if price is None:
            price=response.xpath('//span[@class="p-price"]/span[@class="p-price"]/span[@class]/text()').extract_first()
        item_url=response.url
        pattern=re.compile(r'\d+')
        idlist=pattern.findall(item_url)
        for i in idlist:
            item_id=i
        
        temp=response.xpath('//em[@class="u-jd"]')
        flag=temp.xpath('string(.)').extract_first()
        if flag is not None:
            flag=flag.strip()
               
        print item_url,item_id
        #print comments
        print price
#         item['item_url']=item_url
#         item['item_id']=item_id
#         item['price']=price
#         item['flag']=flag
# 
#         print item

        yield {
        'item_url':item_url,
        'item_id':item_id,
        'price':price,
        'flag':flag,
        #'comments':comments,
        }
        summmary_url='http://club.jd.com/ProductPageService.aspx?method=GetCommentSummaryBySkuId&referenceId='+item_id
        yield scrapy.Request(summmary_url, callback=self.summary_parse)
        
    def summary_parse(self,response):
        print response
        summaryjson_dict=json.loads(response.body_as_unicode())
        print summaryjson_dict
        item_id=summaryjson_dict.get('SkuId')
        comment_count=summaryjson_dict.get('CommentCount')
        good_rate=summaryjson_dict.get('GoodRate')
        score_1=summaryjson_dict.get('Score1Count')
        score_2=summaryjson_dict.get('Score2Count')
        score_3=summaryjson_dict.get('Score3Count')
        score_4=summaryjson_dict.get('Score4Count')
        score_5=summaryjson_dict.get('Score5Count')      
        for i in range(10):
            i=i+1
            comments_url='http://club.jd.com/review/'+str(item_id)+'-1'+'-'+str(i)+'-0.html'
            print comments_url
        yield{
            'item_id':item_id,
            'comment_count':comment_count,
            'good_rate':good_rate,
            'score1':score_1 ,
            'score2':score_2 ,
            'score3':score_3 ,
            'score4':score_4 ,
            'score5':score_5 ,                     
            } 
        
    
           
 
 
        