# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from datetime import datetime

class SQLitePipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('database.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS uncleaned_used_cars(
                            title TEXT,
                            price TEXT,
                            year TEXT,
                            milage TEXT,
                            transmission TEXT,
                            fuel_type TEXT,
                            body_style TEXT,
                            engine_size TEXT,
                            doors TEXT,
                            location TEXT,
                            link TEXT,
                            datestamp TEXT,
                            timestamp2 TEXT)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        now = datetime.now()
        datestamp = now.strftime("%Y-%m-%d")
        timestamp2 = now.strftime("%H:%M:%S")
        self.curr.execute("""INSERT INTO uncleaned_used_cars values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
            item['title'],
            item['price'],
            item['year'],
            item['milage'],
            item['transmission'],
            item['fuel_type'],
            item['body_style'],
            item['engine_size'],
            item['doors'],
            item['location'],
            item['link'],
            datestamp,
            timestamp2
        ))
        self.conn.commit()
        return item


class SQLitePipelineCarsDetails(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('database.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS details_cars_data(
                            title TEXT,
                            price TEXT,
                            year TEXT,
                            milage TEXT,
                            transmission TEXT,
                            fuel_type TEXT,
                            body_style TEXT,
                            engine_size TEXT,
                            doors TEXT,
                            location TEXT,
                            link TEXT,
                            phone TEXT,
                            name TEXT,
                            address TEXT,
                            mot_expiry TEXT,
                            engine_power TEXT,
                            acceleration TEXT,
                            insurance_group TEXT,
                            fuel_consumption_combined TEXT,
                            car_unique_id TEXT,
                            datestamp TEXT,
                            timestamp2 TEXT,
                            make TEXT,
                            model TEXT)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        now = datetime.now()
        datestamp = now.strftime("%Y-%m-%d")
        timestamp2 = now.strftime("%H:%M:%S")
        self.curr.execute("""INSERT INTO details_cars_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (
            item['title'],
            item['price'],
            item['year'],
            item['milage'],
            item['transmission'],
            item['fuel_type'],
            item['body_style'],
            item['engine_size'],
            item['doors'],
            item['location'],
            item['link'],
            item['phone'],
            item['name'],
            item['address'],
            item['mot_expiry'],
            item['engine_power'],
            item['acceleration'],
            item['insurance_group'],
            item['fuel_consumption_combined'],
            item['car_unique_id'],
            datestamp,
            timestamp2,
            item['make'],
            item['model'],
        ))
        self.conn.commit()
        return item


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class UsedcarsniPipeline:
    def process_item(self, item, spider):
        return item
