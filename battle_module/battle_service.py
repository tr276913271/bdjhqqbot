# -*- coding: UTF-8 -*-
from battle_module.battle_dao import BattleDao

class BattleService:
    def shouldService(self,content):
        if(content=='人物信息'):
            return True
        return False

    def service(self,member):
        dao = BattleDao()
        if(dao.isNewUser(member)):
            dao.insertNewUser(member)
        return dao.selectUser(member).showInfo()
