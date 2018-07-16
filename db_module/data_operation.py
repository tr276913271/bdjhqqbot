#- * -coding: utf - 8 - * -
from db_module.connect_db import DBHelper
from db_module.data_tuple_to_str import DBTStr
import pymysql

class DBTopera:
    # 在theft里创建一行
    # member1 偷窃人 member2 被偷窃人
    def creatTheftUser(self, member1, member2, stealCoin ):
        self.timeToday = time.strftime("%Y-%m-%d", time.localtime())
        self.member1 = int(DBTStr().userIdStr(self.member1))
        self.member2 = int(DBTStr().userIdStr(self.member2))
        DBHelper().insert("INSERT INTO `theft` (`userid`, `coin`, `theftDate`, `theftUserid`) VALUES ('"str(self.member1)"' ,'"str(stealCoin)"','"str(self.timeToday)"', '"str(self.member2)"' )")
        return True