# -*- coding: utf-8 -*-
import time

from ApplicationShow import ApplicationShow
from Dispatch import Dispatch
from UrlManager import UrlManager
from HtmlParser import HtmlParser

# 操作运行程序

"""
    确定要爬取的URL地址
    加入urlManager

    while，判断urlManager中是否有url{

        从urlManager中取出一个待爬取的url
        送入dispatch，爬取获得爬取的url地址和context
        得到的context与爬取的url组成参数，放入ApplicationShow中
        送context进入Parser，分析获得新的url地址
        将url加入urlManager中
    }

    从Application中显示爬取的ApplicationShow
"""


class CrawlerMain(object):


    def __init__(self):
        self.G_STATE_OK = 200
        self.crawMaxCount = -1
        self.crawCountNum = 0


        self.urlManager = UrlManager()
        self.dispatch = Dispatch()
        self.htmlParser = HtmlParser("http://baike.baidu.com")
        self.applicationShow = ApplicationShow()

    def craw(self, url):
        self.urlManager.add_url([url])

        """
         设定计数器，
         如果crawMaxCount > 0 说明需要进行计数，
         生成一个count计数器,最大搜索多少次
         当count计数器大于crawMaxCount的时候停止

         否则，不进行计数
        """
        while self.urlManager.has_next_url():

            if 0 < self.crawMaxCount < self.crawCountNum:
                break

            new_url = self.urlManager.get_url()
            try:
                self.dispatch.launch_request(new_url)
                if self.dispatch.get_status() != self.G_STATE_OK:
                    continue

                context = self.dispatch.get_content()

                self.htmlParser.set_content(context)
                self.htmlParser.parser()

                summary = self.htmlParser.get_summary()
                title = self.htmlParser.get_title

                urls = self.htmlParser.get_new_urls()

            except Exception, e:
                    print "Error " + new_url + " " + str(e)
                    continue


            self.applicationShow.add(new_url, title, summary)
            self.urlManager.add_url(urls)

            self.crawCountNum += 1
            print self.crawCountNum

    def show(self):
        self.applicationShow.show()

    def set_craw_max_count(self, count):
        self.crawMaxCount = count


if __name__ == "__main__":
    main_url = "http://baike.baidu.com/view/1395656.htm"
    crawlerMain = CrawlerMain()
    max_count = 5
    crawlerMain.set_craw_max_count(max_count)
    startTime = time.time()
    crawlerMain.craw(main_url)
    endTime = time.time()

    timeFile = open('time.txt', 'a')
    timeFile.write(str(max_count) + "\t" + str(endTime - startTime) + '\n')
    timeFile.close()

    crawlerMain.show()
