# -*- coding: UTF-8 -*-
from db_module.like_member import LikeMember
from battle_module.battle_dao import BattleDao

def strToInt(content):
    try:
        eid = int(content)
        return True,eid
    except Exception as e:
        return False,0

def registerB(member,content):
    register(member)
    if(LikeMember().likeMemberBe(content)==False):
        register(content)
    b = LikeMember().likeMember(content)
    register(b)
    return b

def register(member):
    dao = BattleDao()
    if(dao.isNewUser(member)):
        uid = dao.insertNewUser(member)
        dao.insertBattle(uid)
    else:
        uid = dao.selectUid(member)
        if(dao.isNewBattle(uid[0])):
            dao.insertBattle(uid[0])
