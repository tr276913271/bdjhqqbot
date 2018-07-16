#- * -coding: utf - 8 - * -
import random
from db_module.connect_db import DBHelper
from db_module.data_tuple_to_str import DBTStr

class TheftSystem:
    #member1 偷窃人 member2被偷窃人
    def theftFun(self, member1, member2):
        if random.random() < 0.2:
            self.menstr = member1+ '欧尼酱' +'你被对方发现了呢！偷窃失败！蛤你！'
        elif: int(DBTStr().userCoinStr(member2)) < 10 :
            self.menstr = member2 + '欧尼酱的大给币太少了呢，都藏在胖次里了你偷不到了。'
        else:
            self.allCoin = int(DBTStr().userCoinStr(member2))
            minusCoin = round(self.allCoin / 10)
            self.allCoin = self.allCoin - minusCoin
            DBHelper().update("update user set `coin`= '"+str(self.allCoin)+"' where name = '"+member2+"' ")
            self.menstr = member1 + '欧尼酱成功从' + member2 + '欧尼酱那里偷取了' + minusCoin + '个大给币( •̀ ω •́ )y'
        return self.menstr 

            



    