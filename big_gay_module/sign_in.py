#- * -coding: utf - 8 - * -
import time, json, random, pymysql
import db_module.connect_db import DBHelper

db = pymysql.connect("localhost","root","159263","buket" )
class SignInSystem:
    def shoudlService(self, content):
        if content == '大给币':
            return True
        if content == '查询':
            return True
        return False
    
    def service (self, member, content):
        if content == '大给币':
            return self.signIn(member)
        if content == '查询':
            return self.queryIn(member)
    
    #大给币签到
    def signIn(self, member):
        

        #没有用户自动创建
        if len(DBHelper().selectAll("select name from user where name = '"+str(member)+"' ")) == 0:
            DBHelper().insert("INSERT INTO `user` (`name`, `coin`, `coinDate`) VALUES ('"+str(member)+"', 0, NULL)")

        #用户签到变量声明
        timeToday = time.strftime("%Y-%m-%d", time.localtime())
        userCoinDateTuple = DBHelper().selectOne("select coinDate from user where name = '"+str(member)+"' ")
        userCoinDate = userCoinDateTuple[0].__str__()
        #签到
        if userCoinDate != str(timeToday):
            thisCoin = DBHelper().selectOne("select coin from user where name = '"+str(member)+"' ")
            thisCoinStr = thisCoin[0].__str__()
            coinIncrement = random.randint(1,10)
            thisCoin = int(thisCoinStr) + coinIncrement
            thisCoinStr = str(thisCoin)
            DBHelper().update("update user set `coin`='"+thisCoinStr+"' where name = '"+member+"' ")
            DBHelper().update("update user set `coinDate`='"+timeToday+"' where name = '"+member+"' ")
            menstr = '耶~' + member + '欧尼酱今天获取了' + str(coinIncrement) + '个大给币！' + '\n欧尼酱现在一共有' + thisCoinStr + '个大给币哟~'
        else:
            menstr = '欧尼酱今天已经领取过大给币了~再乱来小心扣你大给币！( `д´)'
        return menstr
    # 查询系统
    def queryIn(self, member):
        if len(DBHelper().selectAll("select name from user where name = '"+str(member)+"' ")) == 0:
            menstr = '欧尼酱你还没有大给币哦，先签到领取一个吧~'
        else:
            userCoin = DBHelper().selectOne("select coin from user where name = '"+str(member)+"' ")
            userCoin = userCoin[0].__str__()
            menstr = '欧尼酱有' + userCoin + '个大给币呢~~'
        return menstr


            






        #时间 time.strftime("%Y-%m-%d", time.localtime())
        #print(time.strftime("%Y-%m-%d", time.localtime()))
        #row =DBHelper().selectAll("select name from user where name='test'") 
        #row = row[0]
        #print ('%s' % row)




