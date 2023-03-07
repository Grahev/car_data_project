import scrapy
import re
from ..items import UsedcarItemDetails
import datetime
import csv
import sqlite3

# link = 'https://www.usedcarsni.com/311307371'

class UsedcarsniDetailsSpider(scrapy.Spider):
    name = 'usedcarsni_details'
    custom_settings = {
        'ITEM_PIPELINES': {'usedcarsni.pipelines.SQLitePipelineCarsDetails': 300}
    }
    start_urls = []
    allowed_domains = ['usedcarsni.com']



    def start_requests(self):

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        # id_list = cursor.execute('''SELECT id FROM unique_ids WHERE date(datestamp) = date('now', '-1 day')''').fetchall()
        id_list = cursor.execute('''SELECT id FROM unique_ids WHERE date(datestamp) = date('now')''').fetchall()
        print(id_list)

        for id in id_list:
            url = 'https://www.usedcarsni.com/'+str(id[0])
            yield scrapy.Request(url, self.parse, cb_kwargs={'id': id[0]})
    
   

    def parse(self, response, id):
        title = response.css('h1.car-detail-header__title a::text').get()
        if title is None:
            title = response.css('h1.h1-title-bar-with-wrap::text').get()

        title = title.strip() if title else None
        link = response.css('h1.car-detail-header__title a::attr(href)').get()

        #get all tech data
        tech_spec_container = response.css('div#tech-spec table')
        rows = tech_spec_container.xpath('.//tr')

        tech_data = {}

        for row in rows:
            key = row.css('td:nth-child(1)::text').get()
            key = key.strip() if key else None
            value = row.css('td:nth-child(2)::text').get()
            value = value.strip() if value else None
            tech_data[key] = value

        #get all short info
        short_info_container = response.css('div.technical-params')
        rows = short_info_container.xpath('.//div[@class="row"]')

        for row in rows:
            key = row.css('div.technical-headers::text').get()
            key = key.strip() if key else None
            value = row.css('div.technical-info::text').get()
            value = value.strip() if value else None
            tech_data[key] = value

        #phone and name
        phone = response.css('div.dealer_phone span::text').getall()
        try:
            name = phone[1]
        except:
            name = 'N/A'
        try:
            phone = phone[0]
        except:
            phone = 'N/A'

        #price
        price = response.css('span.y-big-price_green::text').get()
        price = price.strip() if price else None

        #address
        address = response.css('address::text').getall()

        address = list(filter(lambda x: x.strip(), address))
        address = [s.strip() for s in address]
        address = ', '.join(address)

        print(tech_data)

        item = UsedcarItemDetails()
        item['car_unique_id'] = id
        item['year'] = ''
        item['title'] = title
        item['price'] = price
        try:
            item['milage'] = tech_data['Mileage']
        except:
            item['milage'] = 'N/A'
        item['transmission'] = tech_data['Transmission']
        item['fuel_type'] = tech_data['Fuel Type']
        item['body_style'] = tech_data['Body Style']
        try:
            item['engine_size'] = tech_data['Engine Size']
        except:
            item['engine_size'] = 'N/A'
        item['doors'] = tech_data['Doors']
        item['color'] = tech_data['Colour']
        item['location'] = tech_data['Location']
        item['timestamp'] = datetime.datetime.now()
        try:
            item['phone'] = phone
        except:
            item['phone'] = 'N/A'
        try:
            item['name'] = name
        except:
            item['name'] = 'N/A'
        item['address'] = address
        item['link'] = link
        try:
            item['mot_expiry'] = tech_data['MOT Expiry']
        except:
            item['mot_expiry'] = 'N/A'
        try:
            item['engine_power'] = tech_data['Engine Power']
        except:
            item['engine_power'] = 'N/A'
        try:
            item['acceleration'] = tech_data['Acceleration (0-62mph)']
        except:
            item['acceleration'] = 'N/A'
        try:
            item['insurance_group'] = tech_data['Insurance Group']
        except:
            item['insurance_group'] = 'N/A'
        try:
            item['fuel_consumption_combined'] = tech_data['Fuel Consumption - Combined']
        except:
            item['fuel_consumption_combined'] = 'N/A'

        item['make'] = ''
        item['model'] = ''
        

        
        yield item
