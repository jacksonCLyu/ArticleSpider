# -*- coding: utf-8 -*-
import re
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/114694/']

    def parse(self, response):
        title = response.xpath('//div[@class="entry-header"]/h1/text()')
        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·","").strip()
        praise_numbers = int(response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0])
        fav_numbers = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        match_re = re.match(".*(\d+).*", fav_numbers)
        if match_re:
            fav_numbers = match_re.group(1)

        comment_numbers = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_re = re.match(".*(\d+).*", comment_numbers)
        if match_re:
            comment_numbers = match_re.group(1)

        content = response.xpath("//div[@class='entry']").extract()

        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()

        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]

        pass
