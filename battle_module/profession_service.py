# -*- coding: UTF-8 -*-
from battle_module.battle_service import BattleService
from db_module.code_db import *
from db_module.connect_db import DBHelper

class ProfessionService:

    def __init__(self):
        self.result = ""

    def shouldService(self,content):
        if(content=='转职信息'):
            return True
        elif(content.find('转职') >= 0):
            return True
        return False

    def service(self,member,content):
        if(content=='转职信息'):
            return self.showProfessionList()
        elif(content.find('转职') >= 0):
            content = content.strip('转职')
            BattleService().register(member)
            self.changeProfession(member,content)
            return self.result
        return self.result

    def showProfessionList(self):
        for p in CodeDBService.CodeDB['职业类型']:
            if(p.code==1):
                continue
            self.result += p.codeName+"\n"
        return self.result

    def changeProfession(self,member,content):
        persion =  BattleService().getPerson(member)
        if(persion.level<5):
            self.result = "大于5级才可以转职哦"
            return False

        for prf in CodeDBService.CodeDB['职业类型']:
            if(prf.codeName=="世界BOSS"):
                self.result = "转职失败"
                return False
            if(prf.codeName==content):
                if(persion.profession.code==1):
                    DBHelper().update("update battle set profession = "+str(prf.code)+",maxhp=maxhp+500,hp=maxhp where userId="+str(persion.userId))
                else:
                    DBHelper().update("update battle set profession = "+str(prf.code)+" where userId="+str(persion.userId))
                self.result = "转职成功，你现在是："+prf.codeName
                return True
        self.result = "转职失败"
        return False
