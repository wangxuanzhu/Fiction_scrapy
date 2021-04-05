import scrapy
from Fiction.items import FictionItem


class LewenSpider(scrapy.Spider):
    name = 'lewen'#乐文小说
    allowed_domains = ['62zw.com']
    # 在下面输入小说详情页地址
    start_urls = ['https://www.62zw.com/book_47331/']

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
