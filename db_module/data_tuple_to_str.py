#- * -coding: utf - 8 - * -
from db_module.connect_db import DBHelper
import pymysql, time

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
    # 查询用户当天的偷窃次数 
    def theftNum(self,member):
        timeToday = time.strftime("%Y-%m-%d", time.localtime())
        memberId = DBHelper().selectOne("select id from user where name = '"+member+"' ")
        memberId = memberId[0].__str__()
        theftNumber = DBHelper().selectOne("select count(*) from theft where userId = '"+memberId+"' and theftDate = '"+timeToday+"'")
        theftNumber = theftNumber[0].__str__()
        return theftNumber

    #查询用户当天被偷窃的次数
    def theBeFtNum(self,member):
        timeToday = time.strftime("%Y-%m-%d", time.localtime())
        memberId = DBHelper().selectOne("select id from user where name = '"+member+"' ")
        memberId = memberId[0].__str__()
        theBeftNumber = DBHelper().selectOne("select count(*) from theft where theftUserid = '"+memberId+"' and theftDate = '"+timeToday+"'")
        theBeftNumber = theBeftNumber[0].__str__()
        return theBeftNumber
    
    #常用串查询单个 模糊搜索
    def thePostOne(self,content):
        content = '%'+ content +'%'
        if len(DBHelper().selectAll("select returnWord from response where keyWord like '"+content+"' ")) == 0:
            menstr = '没有欧尼酱要找的这个串哦'
            return menstr
        else:
            menstrRes = DBHelper().selectOne("select returnWord from response where keyWord like '"+content+"'")
            menstrRes = menstrRes[0].__str__()
            menstrKey = DBHelper().selectOne("select keyWord from response where keyWord like '"+content+"' ")
            menstrKey = menstrKey[0].__str__()
            menstr = menstrKey + '：' + menstrRes
            return menstr

    #常用串查询 列表
    def thePostAll(self, page):
        page = str((page - 1)*5)
        menstr = DBHelper().selectAll("select keyWord,returnWord from response where responseType = '9' limit "+page+",5")
        result = ""
        for t in menstr:
            result += t[0]+":"+t[1]+"\n"
        return result

        