#- * -coding: utf - 8 - * -
from db_module.connect_db import DBHelper
import pymysql

class DBTStr:
    # 查询用户名字，必须存在
    def userSearch(self, member):
        userName = DBHelper().selectOne("select name from user where name = '"+str(member)+"' ")
        userName = userName[0].__str__()
        return userName
    # 查询大给币最后一次领取的日期
    def UserCoinDateStr(self, member):
        userCoinDate = DBHelper().selectOne("select coinDate from user where name = '"+str(member)+"' ")
        userCoinDate = userCoinDate[0].__str__()
        return userCoinDate
    # 查询大给币数量
    def userCoinStr(self,member):
        userCoin = DBHelper().selectOne("select coin from user where name = '"+str(member)+"' ")
        userCoin = userCoin[0].__str__()
        return userCoin
    # 查询 user表里的id
    def userIdStr(self, member):
        userId = DBHelper().selectOne("select id from user where name = '"+str(member)+"' ")
        userId = userId[0].__str__()
        return userId
    # 查询 theft 里的useid
    def theftUserId(self, member):
        theftUserId = DBHelper().selectOne("select userid from theft where name = '"+str(member)+"' ")
        theftUserId = theftUserId[0].__str__()
        return theftUserId
        