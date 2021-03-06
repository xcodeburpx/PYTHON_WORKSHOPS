# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from pymongo import MongoClient

class MongoDbPipeline(object):

    # Name if Pipeline
    collection="Quotes"

    # Create instance
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    # Return new instance of Pipeline
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db =crawler.settings.get('MONGO_DB')
        )

    # Do something if spider is opened
    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    # Do something if spider is closed
    def closed_spider(self, spider):
        self.client.close()


    def process_item(self, item, spider):
        self.db[self.collection].insert_one(dict(item))
        return item
