# coding=UTF-8
# 执行数据库的相关操作

import pymysql

class Doing_mysql(object):

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root_psw', db='baike', charset='utf8')
        self.cur = self.conn.cursor()
        # self.cur.execute('USE baike')  # 后面修改成自动创建数据表
        print '数据库已连接'

    def do_reset_mysql(self, table_name, sql, values):# 对数据进行更近或增加操作
        self.cur.execute('USE '+table_name)
        self.cur.execute(sql, values) # 执行相应的SQL语句，对应数据更新进数据库
        self.conn.commit()

    def do_select_mysql(self, sql):
        return self.cur.execute(sql)

    # 创建个人表
    def do_create_table(self, username):
        # 首先检测数据库中是否存在该username的table
        print 'username: ',username
        sql_check = 'SELECT TABLE_NAME FROM information_schema.`TABLES` WHERE TABLE_SCHEMA=\'baike\' AND TABLE_NAME="' +unicode(username, 'utf-8')+'";'
        if self.cur.execute(sql_check)==0:
            # 证明不存在该表
            sql = 'CREATE TABLE ' + username + ' (百度账号 CHAR(10) PRIMARY KEY,头像图片链接 CHAR(200), 百科等级 CHAR(3), 通过版本 CHAR(3), 优质版本 CHAR(3), 特色词条 CHAR(3), 提交版本 CHAR(3), 通过率 CHAR(3), 创建版本 CHAR(3), 财富值 CHAR(3));'
            self.cur.execute(sql)
            self.conn.commit()
        else:
            # 存在该表，不用新建表格
            return

    # 更新个人信息至百度百科个人账号表
    def do_add_userinfo(self, username, user_pic_url, user_level, tongguo, youzhi, tese, tijiao, tongguolv, chuangjian, caifuzhi):
        sql = 'insert into '+username+' (百度账号, 头像图片链接, 百科等级, 通过版本, 优质版本, 特色词条, 提交版本, 通过率, 创建版本, 财富值) ' \
              'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE ' \
              '百度账号=百度账号, 头像图片链接=头像图片链接, 百科等级=百科等级, 通过版本=通过版本 , ' \
              '优质版本=优质版本 , 特色词条=特色词条 , 提交版本=提交版本 , 通过率=通过率 , 创建版本=创建版本 , 财富值=财富值'
        self.cur.execute(sql,(username, user_pic_url, user_level, tongguo, youzhi, tese, tijiao, tongguolv, chuangjian, caifuzhi))
        self.conn.commit()

    def do_end_sql(self):
        self.cur.close()
        self.conn.close()

# Error : You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''伏久飞天', 'http://wwww', 1, 0 ,0 ,0 ,0 ,0 ,0,0) VALUES (%s, %s, %s, %s, %s' at line 1