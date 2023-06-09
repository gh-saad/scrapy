# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class FiverscraperPipeline:
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline:
    def __init__(self):
        self.name_seen = set()
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['title'][0] in self.name_seen:
            raise DropItem("Duplicates item Found {item!r}")
        else:
            self.name_seen.add(adapter['title'][0])
            return item