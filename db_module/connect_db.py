#- * -coding: utf - 8 - * -
import pymysql


class DBHelper:
    def getConnection(self):
        return pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="1991",db="buket",charset="utf8")

    def selectOne(self,sql):
        conn = self.getConnection()
        cur = conn.cursor()
        cur.execute(sql)
        one = cur.fetchone()
        conn.close()
        return one

    def selectAll(self,sql):
        conn = self.getConnection()
        cur = conn.cursor()
        cur.execute(sql)
        all = cur.fetchall()
        conn.close()
        return all

    def update(self,sql):
        conn = self.getConnection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()

    def insert(self,sql):
        conn = self.getConnection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
        return cur.lastrowid

    def delete(self,sql):
        self.update(sql)

if __name__ == '__main__':
    print (DBHelper().insert("INSERT INTO `user` (`name`, `coin`, `coinDate`, `thiefDate`) VALUES ('assa', NULL, NULL, NULL)"))
    print (DBHelper().selectOne("select * from user where id=111"))
    print (DBHelper().selectAll("select * from user where name='aaq'"))
    print (DBHelper().update("update user set `coinDate`='2009-09-09' where id=1"))
    print (DBHelper().delete("delete from user where name='assa'"))
