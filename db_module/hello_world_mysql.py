#- * -coding: utf - 8 - * -
import pymysql

# 打开数据库连接
conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="1991",db="buket",charset="utf8")
"""------------查询------------------------"""
# 使用 cursor() 方法创建一个游标对象 cursor
cur = conn.cursor()
sql = "select * from user"
# 执行
cur.execute(sql)
# 获取所有数据
rows = cur.fetchall()
for dr in rows:
    print(dr)
"""-------------增加-----------------------"""
#增加
sql = """INSERT INTO `user` (`name`, `coin`, `coinDate`, `thiefDate`) VALUES ('assa', NULL, NULL, NULL);"""
cur.execute(sql)
conn.commit()

"""----------------修改--------------------"""

sql = "update user set name='aaq' where id=1"
try:
    # 执行SQL语句
    cur.execute(sql)
    # 提交到数据库执行
    conn.commit()
except:
    # 发生错误时回滚
    conn.rollback()
"""---------删除---------------------------"""
sql = "delete from user where name='assa'"
cur.execute(sql)
conn.commit()
# 关闭数据库连接
conn.close()
