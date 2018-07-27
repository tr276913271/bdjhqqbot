# -*- coding: UTF-8 -*-
from db_module.connect_db import DBHelper
from battle_module.person import Person
class BattleDao:

    def selectActiveBoss(self):
        bossId =  DBHelper().selectOne("select activeBossId from activeboss limit 0,1")
        boss = self.selectUserByUserId(bossId[0])
        return boss

    def isNewUser(self,member):
        result = DBHelper().selectOne("select * from user where name='"+str(member)+"'")
        if(result==None):
            return True
        return False

    def isNewBattle(self,id):
        result = DBHelper().selectOne("select * from battle where userId="+str(id)+"")
        if(result==None):
            return True
        return False

    def selectUid(self,member):
        uid = DBHelper().selectOne("select id from user where name='"+str(member)+"'")
        return uid

    def insertBattle(self,uid):
        dao = DBHelper()
        p = Person(uid)
        dao.insert("insert into battle(`level`, `hp`, `experience`, `attack`, `defense`, `head`, `body`, `weapon`, `userId`,`maxhp`,`profession`) VALUES (\
            1,1000, 0,"+str(p.attack())+","+str(p.defensive())+",1,3,2, '"+str(uid)+"',1000,1)")
        dao.insert("insert into package(`userId`, `equipId`) VALUES ("+str(uid)+",1)")
        dao.insert("insert into package(`userId`, `equipId`) VALUES ("+str(uid)+",2)")
        dao.insert("insert into package(`userId`, `equipId`) VALUES ("+str(uid)+",3)")

    def insertNewUser(self,member):
        db = DBHelper()
        uid = db.insert("insert into user(`name`, `coin`, `coinDate`,`userType`) VALUES ('"+str(member)+"',0, NULL,1)")
        return uid

    def selectUser(self,member):
        db = DBHelper()
        uid = self.selectUid(member)
        if(not uid==None):
            p = Person(member)
            p.initWithDB(db.selectOne("select * from battle where userId="+str(uid[0])))
            return p

    def selectUserByUserId(self,userId):
        db = DBHelper()
        p = Person(self.selectUserName(userId))
        p.initWithDB(db.selectOne("select * from battle where userId="+str(userId)))
        return p

    def updateCoin(self,coin,userId):
        DBHelper().update("update user set `coin` = `coin`+"+str(coin)+" where id = "+str(userId))

    def selectCoin(self,userId):
        return DBHelper().selectOne("select `coin` from user where id = "+str(userId))

    def selectUserName(self,userId):
        name = DBHelper().selectOne("select name from user where id="+str(userId))
        return name[0]
    def updateBattleInfo(self,p):
        db = DBHelper()
        db.update("update battle set level="+str(p.level)+",hp="+str(p.hp)+",experience="+str(p.exp)+",maxhp="+str(p.maxhp)+" where userId="+str(p.userId))
