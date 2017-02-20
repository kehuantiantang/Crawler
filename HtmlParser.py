# -*- coding: utf-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup


# Parser, to analyse the html pages
class HtmlParser(object):
    def __init__(self, hostName):
        self.minLength = 1
        self.hostName = hostName
        self.__content = None
        self.__beautifulSoup = None
        self.__url_feature = r'/view/\d+\.htm'

    def set_content(self, content):
        if content is None or content == "":
            raise ValueError("Content is valid !")
        self.__content = content

    # 分析页面，获得url链接
    def parser(self):
        if self.__content == None or self.__content == "":
            raise ValueError("You must first set content in using set_content method")
        self.__beautifulSoup = BeautifulSoup(self.__content, "html.parser", from_encoding="utf-8")

    def get_new_urls(self):
        oldALinks = self.__beautifulSoup.find_all('a', href=re.compile(self.__url_feature))
        newALinks = []

        for link in oldALinks:
            href = link.get('href')
            if href is not None and len(href) > 0:
                newALinks.append(urlparse.urljoin(self.hostName, href))
        return newALinks

    def get_context(self):
        return self.__content

    @property
    def get_title(self):
        if self.__content is None:
            raise ValueError("Content is not valid")
        else:
            # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
            titleClass = self.__beautifulSoup.find("dd", class_="lemmaWgt-lemmaTitle-title")
            if titleClass is None:
                raise ValueError("Title class is not exist !")

            titleTag = titleClass.find("h1")
            if titleTag is None:
                raise ValueError("Title tag is not exist !")
            return titleTag.get_text().replace('\n', '')



    def get_summary(self):
        if self.__content is None:
            return ""
        else:
            # <div class="lemma-summary" label-module="lemmaSummary">
            # <div class="para" label-module="para">
            summaryTag = self.__beautifulSoup.find("div", class_="lemma-summary")

            if summaryTag is None or self.__is_shorter_than_minLength(summaryTag.get_text()):
                summaryTag = self.__beautifulSoup.find("div", class_="para")
            if summaryTag is None or self.__is_shorter_than_minLength(summaryTag.get_text()):
                raise ValueError("Summary Tag is not exist !")
            return summaryTag.get_text().replace('\n', '')

    def get_beautiful_soup(self):
        return self.__beautifulSoup

    # def set_host_name(self, host):
    #     self.hostName = host


    def __is_shorter_than_minLength(self, content):
        return len(re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", content)) < self.minLength



# html_doc = """
# soup = BeautifulSoup(html_doc, "html.parser")
# print soup.a
# print soup.title.name
# print soup.title.parent.name
# print soup.p
# print soup.p['class']
#
# links = soup.find_all('a')
# for link in links:
#     print link.get_text()
# print soup.find(id="link3")
# print soup.p.get_text()
