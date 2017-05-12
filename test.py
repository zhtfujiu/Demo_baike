# coding=UTF-8
# http://baike.baidu.com/search/none?word=wwwwwww&pn=0&rn=10&enc=utf8
# 👆这是词条不存在时的url

# http://baike.baidu.com/item/%E6%AF%9B%E6%B3%BD%E4%B8%9C/113835
# 👆这是词条存在时的url

# 登录时，如果登录不成功，则还是原来的登录url
# https://passport.baidu.com/v2/?login
url1 = 'https://passport.baidu.com/v2/?login'
url2 = 'https://passport.baidu.com/v2/?login'
# print url1==url2

url3 = 'http://baike.baidu.com/search/none?word=wwwwwww&pn=0&rn=10&enc=utf8'
url4 = 'http://baike.baidu.com/item/%E6%AF%9B%E6%B3%BD%E4%B8%9C/113835'

# print url3.find('ai')
# print 'search/none' in url3

# import pymysql
# conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root_psw', db='information_schema', charset='utf8')
# cur = conn.cursor()
# sql_check = 'SELECT TABLE_NAME FROM information_schema.`TABLES` WHERE TABLE_SCHEMA = \'baike\' AND TABLE_NAME=\'\u4f0f\u4e45\u98de\u5929\';'
# print cur.execute(sql_check)>0
# if cur.execute(sql_check) is not None:
#     print True
# # print
# # \u4f0f\u4e45\u98de\u5929
# print unicode('伏久飞天','utf-8')
# print u'\u4f0f\u4e45\u98de\u5929'
# print u'zzz'
# print '\u4f0f\u4e45\u98de\u5929'.decode()
# str1 = '\xe4\xbc\x8f\xe4\xb9\x85\xe9\xa3\x9e\xe5\xa4\xa9'
# #.encode(encoding='utf-8')
# print str1.decode('unicode_escape')  # 终于可以转码成功

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
# #s_lg_img
# <img id="s_lg_img" src="https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png" width="270" height="129">
# //*[@id="s_lg_img"]
# //*[@id="s_lg_img"]

driver.find_element_by_id("s_lg_img").get_attribute()