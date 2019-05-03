# -*- coding: utf-8 -*-
import re
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/114690/']

    def parse(self, response):
        """
        获取文章列表中的文章 url 并交给解析函数进行具体字段解析
        获取下一页 url 并交给scrapy 下载
        """
        title = response.xpath('//div[@class="entry-header"]/h1/text()')
        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract_first("").strip().replace("·","").strip()
        praise_numbers = int(response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract_first("0"))
        fav_numbers = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract_first(0)
        match_re = re.match(".*?(\d+).*", fav_numbers)
        if match_re:
            fav_numbers = match_re.group(1)

        comment_numbers = response.xpath("//a[@href='#article-comment']/span/text()").extract_first("")
        match_re = re.match(".*?(\d+).*", comment_numbers)
        if match_re:
            comment_numbers = match_re.group(1)

        content = response.xpath("//div[@class='entry']").extract()

        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()

        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)

        #css 选择器选择
        title = response.css(".entry-header h1::text").extract()

        create_date = response.css("p.entry-meta-hide-on-mobile::text").extract_first("").strip().replace("·","").strip()

        praise_numbers = int(response.css(".vote-post-up h10::text").extract_first("0"))

        fav_numbers = response.css(".bookmark-btn::text").extract_first(0)

        match_re = re.match(".*?(\d+).*", fav_numbers)
        if match_re:
            fav_numbers = match_re.group(1)

        comment_numbers = response.css("a[href='#article-comment'] span::text").extract_first("")
        match_re = re.match(".*?(\d+).*", comment_numbers)
        if match_re:
            comment_numbers = match_re.group(1)

        content = response.css("div.entry").extract_first("")

        tag_list = response.css("p.entry-meta-hide-on-mobile a::text").extract()

        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]

        tags = ",".join(tag_list)

        pass
