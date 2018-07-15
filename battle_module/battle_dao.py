# -*- coding: UTF-8 -*-
from db_module.connect_db import DBHelper
from battle_module.person import Person
class BattleDao:
    def isNewUser(self,member):
        result = DBHelper().selectOne("select * from user where name='"+str(member)+"'")
        if(result==None):
            return True
        return False

    def insertNewUser(self,member):
        db = DBHelper()
        uid = db.insert("insert into user(`name`, `coin`, `coinDate`, `thiefDate`) VALUES ('"+str(member)+"',0, NULL, NULL)")
        p = Person(member)
        db.insert("insert into battle(`level`, `hp`, `experience`, `attack`, `defense`, `head`, `body`, `weapon`, `userId`) VALUES (\
            1,100, 0,"+str(p.attack())+","+str(p.defensive())+",1,3,2, '"+str(uid)+"')")

    def selectUser(self,member):
        db = DBHelper()
        uid = db.selectOne("select id from user where name='"+str(member)+"'")
        if(not uid==None):
            p = Person(member)
            p.initWithDB(db.selectOne("select * from battle where userId="+str(uid[0])))
            return p
