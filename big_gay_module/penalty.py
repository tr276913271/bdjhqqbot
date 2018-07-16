#- * -coding: utf - 8 - * -
from db_module.connect_db import DBHelper
from db_module.data_tuple_to_str import DBTStr

class PenaltyGaybi:
    def buckle(self, member,coinPen):
        self.allCoin = int(DBTStr().userCoinStr(member))
        if (self.allCoin - coinPen > 0):
            self.allCoin = self.allCoin - coinPen
        else:
            self.allCoin = 0
        DBHelper().update("update user set `coin`= '"+str(self.allCoin)+"' where name = '"+member+"' ")
        self.menstr = '你不乖了吧！你被扣掉'+ str(coinPen) + '个大给币了！'
        return self.menstr
        


