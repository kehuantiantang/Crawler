# -*- coding: utf-8 -*-


class UrlManager(object):

    #创建一个新旧集合列,old代表已经爬取的,new代表将要爬取的,
    #避免页面之间相互引用
    def __init__(self):
        self.new_set = set()
        self.old_set = set()

    def add_url(self, urls):
        for url in urls:
            if url not in self.new_set and url not in self.old_set:
                self.new_set.add(url)

    def has_next_url(self):
        return len(self.new_set) != 0

    def get_url(self):
        new_url =  self.new_set.pop()
        self.old_set.add(new_url)
        return new_url