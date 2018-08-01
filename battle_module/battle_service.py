# -*- coding: UTF-8 -*-
from battle_module.battle_dao import BattleDao
from db_module.action_dao import ActionDao
from db_module.like_member import LikeMember
import math,random
from battle_module.boss import BossService
from battle_module.weapon_service import *
from battle_module.monster import MonsterServie

class BattleService:
    def shouldService(self,content):
        print("LOG:content"+content)
        if(content=='人物信息'):
            return True
        if(content=='鸡盒'):
            return True
        if(content=='挑战'):
            return True
        if(content=='买药'):
            return True
        if(content.find('喂饼@') >= 0):
            return True
        if(content=='世界首领'):
            return True
        if(content.find('决斗@') >= 0):
            return True
        if(content=='首领初始化'):
            return True
        if(content=='交任务'):
            return True
        if(content.find('任务') >= 0):
            content = content.strip('任务')
            flag = weapon_service.strToInt(content)
            return flag
        return False

    def service(self,member,content):
        if(content=='人物信息'):
            dao = BattleDao()
            self.register(member)
            return dao.selectUser(member).showInfo()
        if(content=='鸡盒'):
            self.register(member)
            return self.getCheckenBox(member)
        if(content=='挑战'):
            self.register(member)
            return self.challenge(member)
        if(content=='世界首领'):
            self.register(member)
            return BattleDao().selectActiveBoss().showInfo()
        if(content.find('决斗@') >= 0):
            content = content.strip('决斗@')
            content = self.registerB(member,content)
            return self.battleService(member,content)
        if(content=='买药'):
            self.register(member)
            return self.buyMedicine(member)
        if(content.find('喂饼@') >= 0):
            content = content.strip('喂饼@')
            content = self.registerB(member,content)
            return self.eatMedicine(member,content)
        if(content=='首领初始化'):
            return BossService().initBoss()
        if(content=='交任务'):
            return MonsterServie().submit(member)
        if(content.find('任务') >= 0):
            self.register(member)
            content = content.strip('任务')
            eid = int(content)
            return MonsterServie().service(member,eid)

    def eatMedicine(self,a,b):
        pa = self.getPerson(a)
        pb = self.getPerson(b)
        dao = BattleDao()
        coin = dao.selectCoin(pa.userId)
        if(coin[0]<20):
            return "20大给币才能喂饼哦"
        pb.hp = pb.maxhp
        dao.updateBattleInfo(pb)
        dao.updateCoin(-20,pa.userId)
        return str(pb.name)+"血量已经恢复了哦"

    def buyMedicine(self,member):
        p = self.getPerson(member)
        dao = BattleDao()
        coin = dao.selectCoin(p.userId)
        if(coin[0] < 20):
            return "20大给币一瓶药哦"
        p.hp = p.maxhp
        dao.updateBattleInfo(p)
        dao.updateCoin(-20,p.userId)
        return str(member)+"血量已经恢复了哦"

    def challenge(self,member):
        dao = BattleDao()
        boss = dao.selectActiveBoss()
        a = dao.selectUser(member)
        result,flag,process = a.battleWith(boss)
        dao.updateBattleInfo(a)
        dao.updateBattleInfo(boss)
        if(flag):
            result += BossService().handleAfterChallange(process,a,boss)
        return result

    def registerB(self,member,content):
        self.register(member)
        if(LikeMember().likeMemberBe(content)==False):
            self.register(content)
        b = LikeMember().likeMember(content)
        self.register(b)
        return b

    def register(self,member):
        dao = BattleDao()
        if(dao.isNewUser(member)):
            uid = dao.insertNewUser(member)
            dao.insertBattle(uid)
        else:
            uid = dao.selectUid(member)
            if(dao.isNewBattle(uid[0])):
                dao.insertBattle(uid[0])

    def battleService(self,a,b):
        dao = BattleDao()
        pa = dao.selectUser(a)
        pb = dao.selectUser(b)
        if(pa.userId==pb.userId):
            return "自己打自己，你怎么不上天"
        if(ActionDao().selectCount(1,pa.userId)>4):
            return "今天已经超过决斗次数了哦，去[挑战]世界首领吧"
        if(ActionDao().selectCount(1,pb.userId)>4):
            return "他今天已经超过决斗次数了哦，去[挑战]世界首领吧"
        result,flag,process = pa.battleWith(pb)
        dao.updateBattleInfo(pa)
        dao.updateBattleInfo(pb)
        if(flag):
            ActionDao().insert(1,pa.userId)
            ActionDao().insert(1,pb.userId)
        return result

    def getCheckenBox(self,member):
        p = self.getPerson(member)
        if(ActionDao().selectCount(2,p.userId)>2):
            return "今天已经领过鸡盒了哦，暴食肥肥！！"
        p.hp+=2000
        if(p.hp>=p.maxhp):
            p.hp = p.maxhp
        ActionDao().insert(2,p.userId)
        BattleDao().updateBattleInfo(p)
        return "欧尼酱领取了鸡盒 HP 恢复了2000 点"

    def getPerson(self,member):
        dao = BattleDao()
        if(dao.isNewUser(member)):
            return None
        else:
            uid = dao.selectUid(member)
            if(dao.isNewBattle(uid[0])):
                return None
        return dao.selectUser(member)
