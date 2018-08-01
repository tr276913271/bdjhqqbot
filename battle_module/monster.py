#- * -coding: utf - 8 - * -
from battle_module.person import Person
from battle_module.battle_dao import BattleDao
from battle_module.equipment_db import EquipmentDB
from battle_module.package_dao import PackageDao
from db_module.action_dao import ActionDao
import  time,random

level1T = (1,1,1000,0,000,000,1,3,2,0,1000,15)
level2T = (1,1,2000,0,100,100,1,3,2,0,2000,15)
level3T = (1,1,4000,0,200,200,1,3,2,0,4000,15)

class MonsterServie(object):
    taskMap = {}
    def __init__(self):
        self.level1 = Person("贪食的肥肥")
        self.level1.initWithDB(level1T)
        self.level2 = Person("Bog")
        self.level2.initWithDB(level2T)
        self.level3 = Person("黑暗中的人")
        self.level3.initWithDB(level3T)
        self.result = ""
    def submit(self,member):
        if(member in MonsterServie.taskMap):
            taskBean = MonsterServie.taskMap[member]
            if(taskBean.isBefore()):
                return "还没有到任务地点哦，请在"+taskBean.getSubmitTimeInterval()+"时间段 [交任务]！"
            elif (taskBean.isAfter()):
                del MonsterServie.taskMap[member]
                return "该任务在"+taskBean.getSubmitTimeInterval()+"时间段提交，任务提交窗口关闭了，请重新接任务吧。"
            else:
                r = self.hunt(member,taskBean.type)
                return r
        return "还没有任务可交哦，试试领取[任务ID]吧"

    def service(self,member,type):
        person = BattleDao().selectUser(member)
        if(type==1):
            if(ActionDao().selectCount(5,person.userId)>2):
                return "初级任务领取到达上限，看看[任务2]吧"
            return self.hunt(member,type)
        if(member in MonsterServie.taskMap):
            return "已经领取了"+MonsterServie.taskMap[member].type+"任务，去[交任务]看看吧！"
        else:
            if(ActionDao().selectCount(3,person.userId)>2):
                return "中级任务领取到达上限，看看[任务3]吧"
            return self.getTask(member,type)
            if(ActionDao().selectCount(4,person.userId)>2):
                return "高级任务领取到达上限，去打世界首领[挑战]吧"
            return self.getTask(member,type)

    def getTask(self,member,type):
        stamp = int(time.time())
        if(type==2):
            self.result = "领取中级任务! 请10分钟后[交任务]领取奖励，交接时间窗口：60分钟\n"
            MonsterServie.taskMap[member] = TaskBean(2,stamp,stamp+600,stamp+6000)
        if(type==3):
            self.result = "领取高级任务! 请30分钟后[交任务]领取奖励，交接时间窗口：5分钟\n"
            MonsterServie.taskMap[member] = TaskBean(3,stamp,stamp+1800,stamp+2100)
        return self.result

    def hunt(self,member,type):
        dao = BattleDao()
        actionDao = ActionDao()
        person = dao.selectUser(member)
        if(type==1):
            self.level1.level  = person.level
            self.result = "你来到了贪食肥肥Neet之处!肥肥正在吃鸡盒！讨伐开始\n"
            result,flag,process = person.battleWith(self.level1)
            self.result += result
            self.level1.hp = self.level1.maxhp
            dao.updateBattleInfo(person)
            if(flag and person.hp>0):
                self.bootySend(person,[1,2,3,11])
                actionDao.insert(5,person.userId)
        elif (type ==2):
            self.level2.level  = person.level * 2
            self.result = "你来到了Bog城堡!Bog们正在刷A岛！讨伐开始\n"
            result,flag,process = person.battleWith(self.level2)
            self.result += result
            self.level2.hp = self.level2.maxhp
            dao.updateBattleInfo(person)
            if(flag):
                del MonsterServie.taskMap[member]
                if(person.hp>0):
                    self.bootySend(person,[12,13,15])
                    actionDao.insert(3,person.userId)
        elif (type ==3):
            self.level3.level  = person.level * 5
            self.result = "你来到了尿尿屋地下室!黑暗中有人向你袭来！讨伐开始\n"
            result,flag,process = person.battleWith(self.level3)
            self.result += result
            self.level3.hp = self.level3.maxhp
            dao.updateBattleInfo(person)
            if(flag):
                del MonsterServie.taskMap[member]
                if(person.hp>0):
                    self.bootySend(person,[17,14,17,16])
                    actionDao.insert(4,person.userId)
        return self.result

    def bootySend(self,person,list):
        dao = PackageDao()
        random.shuffle(list)
        for id in list:
            if(not EquipmentDB.EDB[id] == None):
                if(random.randint(0,100)<EquipmentDB.EDB[id].probability):
                    self.result += person.name+"获得了"+EquipmentDB.EDB[id].name+"!\n"
                    dao.insert(person.userId,id)
                    return ""

class TaskBean:
    def __init__(self,type,timeStamp,closeStart,closeEnd):
        self.type = type
        self.timeStamp = timeStamp
        self.closeStart = closeStart
        self.closeEnd = closeEnd
    def isBefore(self):
        stamp = int(time.time())
        if(stamp<self.closeStart):
            return True
        return False
    def isAfter(self):
        stamp = int(time.time())
        if(stamp > self.closeEnd):
            return True
        return False
    def getSubmitTimeInterval(self):
        return time.strftime("%H:%M:%S", time.localtime(self.closeStart))+"~"+time.strftime("%H:%M:%S", time.localtime(self.closeEnd))
