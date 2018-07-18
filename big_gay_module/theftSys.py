#- * -coding: utf - 8 - * -
import random, time
from db_module.connect_db import DBHelper
from db_module.data_tuple_to_str import DBTStr

class TheftSystem:
    #member1 偷窃人 member2被偷窃人
    def theftFun(self, member1, member2):
        self.member1 = member1
        self.member2 = member2
        self.userCoin = DBTStr().userCoinStr(self.member2)
        
        self.userCoin = int(self.userCoin)
        if random.random() < 0.5:
            timeToday = time.strftime("%Y-%m-%d", time.localtime())
            member1userid = DBTStr().userIdStr(self.member1)
            member2userid = DBTStr().userIdStr(self.member2)

            DBHelper().insert("INSERT INTO `theft` (`userId`, `coin`, `theftDate`, `theftUserid`) VALUES ('"+str(member1userid)+"', '0', '"+str(timeToday)+"' ,'"+str(member2userid)+"')")
            self.menstr = self.member1+ '欧尼酱你被对方发现了呢！偷窃失败！蛤你！'
        elif self.userCoin < 10:
            self.menstr = self.member2 + '的大给币太少了呢，都藏在胖次里了欧尼酱偷不到了。'
        else:
            self.allCoin = int(DBTStr().userCoinStr(self.member2))
            minusCoin = round(self.allCoin / 20)
            self.allCoin = self.allCoin - minusCoin
            DBHelper().update("update user set `coin`= '"+str(self.allCoin)+"' where name = '"+self.member2+"' ")
            self.allCoin1 = int(DBTStr().userCoinStr(self.member1))
            self.allCoin1 = self.allCoin1 + minusCoin
            DBHelper().update("update user set `coin`= '"+str(self.allCoin1)+"' where name = '"+self.member1+"'")






            timeToday = time.strftime("%Y-%m-%d", time.localtime())
            member1userid = DBTStr().userIdStr(self.member1)
            member2userid = DBTStr().userIdStr(self.member2)
            DBHelper().insert("INSERT INTO `theft` (`userId`, `coin`, `theftDate`, `theftUserid`) VALUES ('"+str(member1userid)+"', '"+str(minusCoin)+"', '"+str(timeToday)+"' ,'"+str(member2userid)+"')")
            self.menstr = str(self.member1) + '欧尼酱成功从' + str(self.member2) + '欧尼酱那里偷取了' + str(minusCoin) + '个大给币( •̀ ω •́ )y'
        return self.menstr 