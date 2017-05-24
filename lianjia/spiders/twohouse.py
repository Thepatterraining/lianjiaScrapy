# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from lianjia.items import LianjiaItem
import re


class TwohouseSpider(CrawlSpider):
    name = 'twohouse'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['http://bj.lianjia.com/xiaoqu']

    rules = (
        Rule(LinkExtractor(allow=r'/xicheng/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        item = LianjiaItem()
        title_css = 'div.content div.leftContent ul.listContent li.xiaoquListItem div.info div.title a::text'
        item['name'] = response.css(title_css).extract()
        url_css = "div.content div.leftContent ul.listContent li.xiaoquListItem div.info div.title a::attr(href)"
        item['url'] = response.css(url_css).extract()
        match = re.match(r'https://bj.lianjia.com/xiaoqu/(.*?)/',item['url'])
        item['xiaoquid'] = match.group(1)
        return item

