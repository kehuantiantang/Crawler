# -*- coding: utf-8 -*-


class UrlManager(object):

    #创建一个新旧集合列,old代表已经爬取的,new代表将要爬取的,
    #避免页面之间相互引用
    def __init__(self):
        self.__new_set = set()
        self.__old_set = set()

    def add_url(self, urls):
        for url in urls:
            if url not in self.__new_set and url not in self.__old_set:
                self.__new_set.add(url)

    def has_next_url(self):
        return len(self.__new_set) != 0

    def get_url(self):
        new_url =  self.__new_set.pop()
        self.__old_set.add(new_url)
        return new_url

    def get_urlSet(self):
        return self.__new_set