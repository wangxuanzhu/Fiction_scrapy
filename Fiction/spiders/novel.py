import scrapy
from Fiction.items import FictionItem


class NovelSpider(scrapy.Spider):
    name = 'qidian'# 起点小说
    allowed_domains = ['qidian.com']
    # 在下面输入小说详情页地址
    start_urls = ['https://book.qidian.com/info/1019544887#Catalog']

    def parse(self, response):
        pages = response.xpath('//div[@id="j-catalogWrap"]//ul[@class="cf"]/li/a/@href')
        novel_name = response.xpath('/html/body/div/div[6]/div[1]/div[2]/h1/em/text()').extract_first()
        # pages = response.xpath('//div[@id="j-catalogWrap"]//ul[@class="cf"]/li/')
        # print(type(pages))
        idx = 0
        for page in pages:
            url = page.extract()
            idx += 1
            # print(url, idx)
            yield response.follow(url=url, meta={'idx': idx, 'novel_name': novel_name}, callback=self.parse_chapter)


    def parse_chapter(self, response):
        idx = response.meta['idx']
        string = response.meta['novel_name']

        title = response.xpath('//h3[@class="j_chapterName"]/span[1]/text()').extract_first().strip()
        content = response.xpath('//div[@class="main-text-wrap "]//div[@class="read-content j_readContent"]').extract_first().strip()

        print(string, type(string))
        print(title)
        novel = string.replace(" ", "")
        title1 = title.replace('!', '！')
        title = title1.replace('?', '？')
        title1 = title.replace('!', '！')
        title = title1.replace('*', '/*')

        item = FictionItem()
        item['idx'] = idx
        item['title'] = title
        item['content'] = content
        item['novel'] = novel
        print(novel, type(novel))
        yield item
