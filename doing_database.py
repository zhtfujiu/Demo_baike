# coding=UTF-8

# 数据筛选及二次开发接口

'''
功能List：
1、完成数据读取并展示
2、转出Excel
3、数据分栏目展示
4、SQL语句接口，提供查询操作
'''

# import xlrd
#
# workbook = xlrd.open_workbook('file1.xlsx')
# print workbook.sheet_names()[0].encode('utf-8')

import pymysql
from doing_mysql import Doing_mysql


class Doing_Database(object):
    def __init__(self):
        # 实例化一个数据库操作对象
        self.doing_mysql = Doing_mysql()

    def do_database(self):
        print '=====数据分析子功能List：=====\n\n' \
              '1、导出词条的相关数据的Excel文件\n' \
              '2、二次开发接口（自定义SQL语句）\n' \
              '3、数据栏目筛选展示\n' \
              '4、返回上层菜单'

        while True:
            order = raw_input('=====请输入要执行的子功能序号：======\n').strip()  # 去除前后空格
            if not order.isdigit():
                # 非法数据，重新输入
                print '*****请输入合法序号！*****'
                continue
            order = int(order)
            if order == 1:
                self.set_entry()
                # 执行导出功能
                self.do_export()

            elif order == 2:
                self.set_entry()
                # 执行自定义SQL操作
                self.do_DIY_sql()

            elif order == 3:
                self.set_entry()
                # 执行数据库栏目title筛选
                self.do_select_title()

            elif order == 4:
                # 本层退出，返回home
                self.doing_mysql.do_end_sql()
                break

            else:
                # 非法数据，重新输入
                print '*****请输入合法序号！*****'
                continue

    # 设置词条名，即对数据表进行选择
    def set_entry(self):
        try:
            while True:
                self.entry = raw_input('请输入要操作的根词条（即要操作的数据表名称）：\n')
                if self.doing_mysql.do_check_is_in(self.entry):
                    # 返回真，证明存在这个词条
                    break
                else:
                    print '本词条不存在'
                    continue

        except Exception, e:
            print e


    # 导出功能
    def do_export(self):
        # data = self.doing_mysql.do_select_mysql('select * from '+unicode(self.entry, 'utf-8'))
        self.doing_mysql.do_ecport2excel(self.entry)

        pass


    # 自定义SQL语句功能
    def do_DIY_sql(self):
        print '本功能为用户提供SQL语言接口，请严格按照MySQL数据库语法输入，否则无法得到预期结果！'




    # 筛选栏目名称
    def do_select_title(self):

        pass


