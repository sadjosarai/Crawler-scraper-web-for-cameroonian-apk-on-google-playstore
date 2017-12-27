import scrapy
from verif.items import VerifItem
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import CrawlSpider



class Crawl_spider(CrawlSpider) :
    name = "test"
    allowed_domains = ["play.google.com"]
    start_urls = ["https://play.google.com/store/search?q=cameroon"]


    #Rules = (
             # Rule (LinkExtractor(allow=(), restrict_xpath('//button[@class="play-button"]',)), callback = "parse", follow = True),

 #)

    def parse(self, response) :

       bases =  response.selector.xpath('//div[@class="details"]/a[@class="title"]')
       for base in bases :
       
          item = VerifItem()
          item["name"] = base.xpath('text()').extract()
          item["link"] = base.xpath('@href').extract()
          item["desc"] = response.selector.xpath('//div[@class="details"]/div[@class="description"]/text()').extract()
          yield item
