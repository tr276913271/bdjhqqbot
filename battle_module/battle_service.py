# -*- coding: UTF-8 -*-
from battle_module.battle_dao import BattleDao
from db_module.action_dao import ActionDao
from db_module.like_member import LikeMember
import math,random
class BattleService:
    def shouldService(self,content):
        print("LOG:content"+content)
        if(content=='人物信息'):
            return True
        if(content=='鸡盒'):
            return True
        print("LOG:find决斗@"+str(content.find('决斗@')))
        if(content.find('决斗@') >= 0):
            return True
        return False

    def service(self,member,content):
        if(content=='人物信息'):
            dao = BattleDao()
            if(dao.isNewUser(member)):
                uid = dao.insertNewUser(member)
                dao.insertBattle(uid)
            else:
                uid = dao.selectUid(member)
                if(dao.isNewBattle(uid[0])):
                    dao.insertBattle(uid[0])
            return dao.selectUser(member).showInfo()
        if(content=='鸡盒'):
            try:
                return self.getCheckenBox(member)
            except:
                return "没有注册哦，@半姬 人物信息 注册"
        if(content.find('决斗@') >= 0):
            content = content.strip('决斗@')
            try:
                print("LOG:likeMember@"+str(LikeMember().likeMember(content)))
                return self.battleService(member,LikeMember().likeMember(content))
            except:
                return "双方有人没有注册哦，@半姬 人物信息 注册"


    def battleService(self,a,b):
        dao = BattleDao()
        pa = dao.selectUser(a)
        pb = dao.selectUser(b)
        if(ActionDao().selectCount(1,pa.userId)>3):
            return "今天已经超过决斗次数了哦，休息下吧"
        if(ActionDao().selectCount(1,pb.userId)>3):
            return "他今天已经超过决斗次数了哦，让他休息下吧"
        result,flag = pa.battleWith(pb)
        dao.updateBattleInfo(pa)
        dao.updateBattleInfo(pb)
        if(flag):
            ActionDao().insert(1,pa.userId)
            ActionDao().insert(1,pb.userId)
        return result

    def getCheckenBox(self,member):
        p = self.getPerson(member)
        if(ActionDao().selectCount(2,p.userId)>1):
            return "今天已经领过鸡盒了哦，暴食肥肥！！"
        p.hp+=500
        if(p.hp>=p.maxhp):
            p.hp = p.maxhp
        ActionDao().insert(2,p.userId)
        BattleDao().updateBattleInfo(p)
        return "欧尼酱领取了鸡盒 HP 恢复了500 点"

    def getPerson(self,member):
        dao = BattleDao()
        if(dao.isNewUser(member)):
            return None
        else:
            uid = dao.selectUid(member)
            if(dao.isNewBattle(uid[0])):
                return None
        return dao.selectUser(member)
