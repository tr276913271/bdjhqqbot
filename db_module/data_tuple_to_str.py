#- * -coding: utf - 8 - * -
from db_module.connect_db import DBHelper
import pymysql

class DBTStr:
    def userSearch(self, member):
        userName = DBHelper().selectOne("select name from user where name = '"+str(member)+"' ")
        userName = userName[0].__str__()
        return userName

    def UserCoinDateStr(self, member):
        userCoinDate = DBHelper().selectOne("select coinDate from user where name = '"+str(member)+"' ")
        userCoinDate = userCoinDate[0].__str__()
        return userCoinDate

    def userCoinStr(self,member):
        userCoin = DBHelper().selectOne("select coin from user where name = '"+str(member)+"' ")
        userCoin = userCoin[0].__str__()
        return userCoin
