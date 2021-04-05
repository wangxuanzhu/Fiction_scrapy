# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FictionPipeline:
    # novel_list = []
    def open_spider(self, spider):
        self.items = []


    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        novel = self.items[0]['novel']
        print(novel)
        filename = './down/%s.html' % novel
        with open(filename, 'w', encoding='utf-8') as f:
            header = '<!DOCTYPE html><html lang="zh"><head><meta charset="UTF-8"></head><body>'
            footer = '</body></html>'
            f.write(header)

            self.items.sort(key=lambda idx: idx['idx'])

            for item in self.items:
                cnt = '<h3>{}</h3>{}<br><hr><br>'.format(item['title'], item['content'])
                f.write(cnt)

            f.write(footer)


