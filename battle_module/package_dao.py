# -*- coding: UTF-8 -*-
from db_module.connect_db import DBHelper

class PackageDao:

    def select(self,userId):
        result = DBHelper().selectAll("select * from package where userId="+str(userId))
        return result

    def selectByUserIdAndEquipId(self,userId,equipId):
        result = DBHelper().selectAll("select * from package where userId="+str(userId)+" and equipId="+str(equipId))
        return result
    def sellByUserIdAndEquipId(self,userId,equipId):
        DBHelper().delete("delete from package where userId="+str(userId)+" and equipId="+str(equipId))
        
    def insert(self,userId,equipId):
        DBHelper().delete("insert into package(`userId`, `equipId`) VALUES ("+str(userId)+","+str(equipId)+")")
