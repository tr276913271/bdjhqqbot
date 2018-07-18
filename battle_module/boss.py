# -*- coding: UTF-8 -*-
from db_module.connect_db import *
from db_module.code_db import *
from battle_module.battle_dao import BattleDao
from battle_module.package_dao import PackageDao
from battle_module.equipment_db import EquipmentDB
import math,random

class BossService:
    def __init__(self):
        self.result=""

    def handleAfterChallange(self,process,a,boss):
        self.insertDps(process,a,boss)
        if(boss.hp<=0):
            self.bootySend(boss)
        return self.result

    def insertDps(self,process,a,boss):
        DBHelper().insert("insert dps(damage,userId,bossId) VALUES("+str(process.aDamage)+","+str(a.userId)+","+str(boss.userId)+")")

    def bootySend(self,boss):
        tupleList = DBHelper().selectAll("SELECT userId,sum(damage) as damage from dps where bossId="+str(boss.userId)+" GROUP BY userId ORDER BY damage desc")
        one = []
        two = []
        three = []
        size = len(tupleList)
        for i in range(size):
            if(i<(size/3)):
                one.append(tupleList[i][0])
            elif(i<(size/3*2)):
                two.append(tupleList[i][0])
            else:
                three.append(tupleList[i][0])
        self.handleExpMoney(one,1)
        self.handleExpMoney(two,2)
        self.handleExpMoney(three,3)
        self.result+="\n"
        self.bootyPackage(tupleList,boss.userId)

    def bootyPackage(self,tupleList,bossId):
        bootys = PackageDao().select(bossId)
        for b in bootys:
            temp = {}
            for record in tupleList:
                temp[record[0]] = random.randint(0,100)
            rd = {"ID":"","NUM":0}
            for record in tupleList:
                if (rd['NUM'] < temp[record[0]]):
                    rd['ID'] = record[0]
                    rd['NUM'] = temp[record[0]]
            self.result += str(BattleDao().selectUserByUserId(rd["ID"]).name)+" 获得了"+str(EquipmentDB.EDB[b[2]].name)+"\n"
        return self.result

    def handleExpMoney(self,list,level):
        dao = BattleDao()
        baseExp = 50
        baseMoney =150
        for record in list:
            pa = dao.selectUserByUserId(record)
            aexp = math.floor((baseExp*level)*round(1+random.uniform(-0.1,0.2),2))
            money = math.floor((baseMoney*level)*round(1+random.uniform(-0.1,0.2),2))
            pa.exp += aexp
            self.result += pa.name + " 获得"+str(aexp)+"点经验 获得"+str(money)+"大给币\n"
            if(pa.exp/100 > pa.level):
                pa.level+=1
                pa.maxhp += 100
                pa.hp += 200
            dao.updateBattleInfo(pa)
            dao.updateCoin(money,pa.userId)
