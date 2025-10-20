# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
import locale


class UindknewsPipeline:
    def process_item(self, item, spider):
        return item

class CleaningdataPipeline:
    def process_item(self, item, spider):
        try:
            locale.setlocale(locale.LC_ALL, 'id_ID')
        except locale.Error:
            print('Locale Indonesia Not Support')
            
        author = item.get('author')
        if author:
            item['author'] = author.strip()
        
        else:
            item['author'] = "Anonymous"
            
        issued = item.get('issued')
        if issued:
            try:
                str_to_date = datetime.strptime(issued,'%B %d, %Y')
                item['issued'] = str_to_date.strftime('%d/%m/%Y')
            
            except ValueError:
                item['issued'] = "Date Not Found"
                    
        else:
            item['issued'] = "Date Not Found"
            
        news_content = item.get('news_content')
        news_content = news_content.replace('/n',' ').replace('/r',' ')
        item['news_content'] = news_content.strip()
        return item
