import scrapy
from .functions import extract_details, get_year
import datetime
import time
import random
import logging


logger = logging.getLogger('mycustomlogger')

class GalgormSpider(scrapy.Spider):
    name = 'usedcarsni'
    custom_settings = {
        'ITEM_PIPELINES': {'usedcarsni.pipelines.SQLitePipeline': 300}
    }
    start_urls = ['https://www.usedcarsni.com/search_results.php?search_type=1&make=0&fuel_type=0&age_from=0&price_from=0&user_type=0&trans_type=0&age_to=0&price_to=0&mileage_to=0&keywords=&distance_enabled=0&distance_postcode=&body_style=0']
    # start_urls = ['https://www.usedcarsni.com/search_results.php?make=1&model=0&keywords=&fuel_type=0&trans_type=0&age_from=0&age_to=0&price_from=0&price_to=0&user_type=0&mileage_to=0&body_style=0&distance_enabled=0&distance_postcode=&homepage_search_attr=1&tab_id=0&search_type=1']

    

    def parse(self,response):
        for list in response.css('article.add-half-row.overflowed-flex.car-line'):

            title = list.css('div.car-title')
            title_text = list.css('strong.car-header.overflowed::text').getall()
            link = 'usedcarsni.com'+ title.css('a').attrib['href']
            details = extract_details(list)
            # time.sleep(random.randint(1,3))

            yield{
                'title': title_text[1].strip(),
                'price': list.css('div.euroPrice.hidden::text').get(),
                'year' : get_year(title),
                'milage': details['milage'],
                'transmission': details['transmission'],
                'fuel_type' : details['fuel_type'],
                'body_style' : details['body_style'],
                'engine_size' : details['engine_size'],
                'doors' : details['doors'],
                'location' : details['location'],
                'timestamp': datetime.datetime.now(),
                'link': link
            }
        try:
            next_page = response.xpath('//*[@id="search-results-list"]/nav[1]/div[2]/ul/li[7]/a').attrib['href']
        except:
            next_page = response.xpath('//*[@id="search-results-list"]/nav[1]/div[2]/ul/li[6]/a').attrib['href']
        print(next_page)
        self.logger.info('Next page is %s', next_page)
        if next_page:
            # url = 'https://www.usedcarsni.com'+ response.xpath('//*[@id="search-results-list"]/nav[2]/div[2]/ul/li[6]/a').attrib['href']
            next_page = response.urljoin(next_page)
            
            yield scrapy.Request(next_page, self.parse)