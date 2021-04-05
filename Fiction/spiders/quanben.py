import scrapy
from Fiction.items import FictionItem


class LewenSpider(scrapy.Spider):
    name = 'quanben'#全本小说
    allowed_domains = ['ad50.com']
    start_urls = ['https://www.qb50.com/book_23146/']

    def parse(self, response):
        pages = response.xpath('/html/body/div[4]/dl/dd/a/@href')
        novel_name = response.xpath('//*[@id="info"]/h1/text()').extract_first()
        idx = 0
        for page in pages:
            url = page.extract()
            idx += 1
            yield response.follow(url=url, meta={'idx': idx, 'novel_name': novel_name}, callback=self.parse_chapter)

    def parse_chapter(self, response):
        idx = response.meta['idx']
        string = response.meta['novel_name']

        title = response.xpath('//*[@id="main"]/h1/text()').extract_first().strip()
        content = response.xpath('//div[@id="main"]//*[@id="content"]').extract_first().strip()

        novel = string.replace(" ", "")
        title1 = title.replace('!', '！')
        title = title1.replace('?', '？')
        title1 = title.replace('!', '！')
        title = title1.replace('*', '/*')
        content2 = content.replace('\xa0\xa0\xa0\xa0', '　　')
        content = content2.replace('<br>', '\n')

        item = FictionItem()
        item['idx'] = idx
        item['title'] = title
        item['content'] = content
        item['novel'] = novel
        yield item
        # print(title)
