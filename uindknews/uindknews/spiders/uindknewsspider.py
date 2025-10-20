import scrapy
from uindknews.items import UindknewsItem


class UindknewsspiderSpider(scrapy.Spider):
    name = "uindknewsspider"
    allowed_domains = ["uindatokarama.ac.id"]
    start_urls = ["https://uindatokarama.ac.id"]

    def parse(self, response):
        posts = response.css('article.elementor-post')
        for post in posts:
            post_link = post.css('h3.elementor-post__title a').attrib['href']
            yield response.follow(post_link, callback=self.get_news_detail)
    
    def get_news_detail(self, response):
        items = UindknewsItem()
        content_tag = response.css("div.elementor-widget-container p::text").getall()
        content_join = ' '.join([content_tag[0], content_tag[1]]) # join praragraf 1 dan 2
        items['url'] = response.url
        items['news_title'] = response.css('div h1.elementor-heading-title::text').get()
        items['author'] = response.xpath("/html/body/div[2]/div[1]/div/div[2]/div/ul/li[2]/a/span/text()").get()
        items['issued']= response.xpath("/html/body/div[2]/div[1]/div/div[2]/div/ul/li[1]/a/span/time/text()").get()
        items['news_content'] = content_join
        yield items
        
        
