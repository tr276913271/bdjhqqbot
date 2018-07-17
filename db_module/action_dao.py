# -*- coding: UTF-8 -*-
from db_module.connect_db import DBHelper
class ActionDao:
    def insert(self,type,userId):
        db = DBHelper()
        db.insert("insert into action(`actionType`, `actionDate`, `actionDateTime`,`userId`) VALUES ("+str(type)+",DATE(NOW()),NOW(),"+str(userId)+")")

    def selectCount(self,type,userId):
        db = DBHelper()
        tuple = db.selectOne("select count(*) from action where actionType="+str(type)+" and userid="+str(userId)+" and actionDate=DATE(NOW())")
        if(tuple == None):
            return 0
        return tuple[0]
