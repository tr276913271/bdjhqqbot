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
            print(uid[0])
            if(dao.isNewBattle(uid[0])):
                dao.insertBattle(uid[0])
        return dao.selectUser(member).showInfo()
