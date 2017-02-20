# -*- coding: utf-8 -*-

# 将爬取好的数据进行装饰，并按照某种形式显示
import codecs
import csv


class ApplicationShow(object):

    def __init__(self):
        self.__data= []

        self.__text_name = None

    def show(self):
        # for data in self.__data:
        #     print data['url'] + data['title'] + data['summary']
        # self.write_to_file('123.txt')
        self.write_to_csv("1.csv")

    # 暂时以数组的形式一行一行信息
    def add(self, url, title, summary):
        self.__data.append({'url' : url, 'title': title, 'summary' : summary })

    # 写csv文件,原始数据文件是utf-8编码
    def write_to_csv(self, fileName):
        if not fileName.endswith('.csv'):
            fileName += '.csv'
        f = open(fileName, 'w')
        f.write(codecs.BOM_UTF8)
        for data in self.__data:
            f.write('%s,%s,%s\n' %(data['url'].encode('utf-8'), data['title'].encode('utf-8'), data['summary'].encode('utf-8') ))
        f.close()
        print "Write to csv finish !"

    # 写入一个文件中,注意原始数据是utf-8编码
    def write_to_file(self, fileName):
        if self.__data is None:
            raise ValueError("Data is empty !")
        writeFile = codecs.open(fileName, 'w', "utf-8")
        for data in self.__data:
            writeFile.write(data['url'] + '\n' + data['title'] + '\n' + data['summary'] + '\n\n')
        writeFile.close()

        print "Write to file finish !"
