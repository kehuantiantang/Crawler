# -*- coding: utf-8 -*-
import cookielib
import urllib2
import re

# 分发器，用来创建url链接，读取数据
class Dispatch(object):

    # 用来全局访问的url
    __m_url = None

    # 默认url地址
    __DEFAULT_URL = 'http://www.baidu.com'

    __m_request = None
    __m_response = None
    __m_page_content = None

    # def __init__(self):
    #     super(Dispatch, self).__init__()

    # construct request to add some header, cookie
    def __construct_request(self, url_request):
        url_request.add_header("user-agent", "Mozilla/5.0")
        return url_request

    # construct cookieHandler
    def __set_construct_cookie_handler(self):
        cookie_container = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_container))
        urllib2.install_opener(opener)

    # launch a new request which depend on url
    def launch_request(self, url = None):
        # 为空则赋予默认值
        if (url != None) :
            pattern = re.compile('^(http://)')
            # url地址是否以http开头
            if pattern.match(url):
                self.__m_url = url
            else:
                self.__m_url = 'http://' + url
        else:
            self.__m_url = self.__DEFAULT_URL

        if self.__m_url is None or self.__m_url == "":
            raise RuntimeError("The global url is unValid ! ")

        self.__m_request = self.__construct_request(urllib2.Request(self.__m_url))
        self.__m_response = urllib2.urlopen(self.__m_request)




    def get_status(self):
        return self.__m_response.getcode()

    def get_content(self):
        self.__m_page_content = self.__m_response.read()
        return self.__m_page_content

    def get_page_length(self):
        if self.__m_page_content is None:
            self.__m_page_content = self.get_content()
        return len(self.__m_page_content)



    def print_context(context):
        print context



# dispatch = Dispatch()
# dispatch.launch_request('http://baike.baidu.com/view/21087.htm')
# print_context(dispatch.get_status())
# print_context(dispatch.get_page_length())
# print_context(dispatch.get_content())


