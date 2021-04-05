from scrapy import cmdline

def select():
    print('现有爬虫项目，输入数字开始爬取：\n'
          '1、乐文小说网爬取\n'
          '2、起点中文网爬取\n'
          '3、全本小说网爬取\n')
    sel = input('请输入爬虫项目：')

    def act(sel):
        urse_select = int(sel)
        if urse_select == 1:
            s1()
        elif urse_select == 2:
            s2()
        else:
            s3()

    act(sel)




def s1():
    cmdline.execute('scrapy crawl lewen '.split())


def s2():
    cmdline.execute('scrapy crawl qidian '.split())


def s3():
    cmdline.execute('scrapy crawl quanben '.split())



if __name__ == "__main__":
    select()