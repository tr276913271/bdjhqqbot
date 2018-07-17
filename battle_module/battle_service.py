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
            uid = dao.insertNewUser(member)
            dao.insertBattle(uid)
        else:
            uid = dao.selectUid(member)
            if(dao.isNewBattle(uid[0])):
                dao.insertBattle(uid[0])
        return dao.selectUser(member).showInfo()

    def battleService(self,content):
        dao = BattleDao()
        uid = dao.selectUid(member)

    def getPerson(self,member):
        dao = BattleDao()
        if(dao.isNewUser(member)):
            return None
        else:
            uid = dao.selectUid(member)
            if(dao.isNewBattle(uid[0])):
                return None
        return dao.selectUser(member)
