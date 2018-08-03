# -*- coding: UTF-8 -*-
from db_module.connect_db import DBHelper
from battle_module.battle_util import *

class BankDao:
    def __init__(self):
        self.db = DBHelper()

    def insert(self,userId):
        self.db.insert("insert bank (userId,money,maxMoney,bankType) VALUES("+str(userId)+",0,500,1)")

    def updateMoney(self,userId,content):
        self.db.update("update bank set money = money+"+str(content)+" where userId="+str(userId))

    def selectByUserId(self,userId):
        return self.db.selectOne("select * from bank where userId="+str(userId))

    def updateLevel(self,userId,maxMoney):
        self.db.update("update bank set bankType = bankType+1, maxMoney = "+str(maxMoney)+" where userId="+str(userId))

class BankService:
    def __init__(self):
        self.result = ""
        self.dao = BankDao()

    def shouldService(self,content):
        if(content=='银行信息'):
            return True
        if(content=='提升银行会员'):
            return True
        if(content=='开户'):
            return True
        if(content.find('存钱') >= 0):
            content = content.strip('存钱')
            flag,eid =  strToInt(content)
            return flag


    def service(self,member,content):
        if(content=='银行信息'):
            register(member)
            return self.showBankInfo(member)
        if(content=='开户'):
            register(member)
            return self.openBank(member)
        if(content=='提升银行会员'):
            register(member)
            return self.updateLevel(member)
        if(content.find('存钱') >= 0):
            register(member)
            content = content.strip('存钱')
            content = int(content)
            return self.saveMoney(member,content)
        if(content.find('取钱') >= 0):
            register(member)
            content = content.strip('取钱')
            content = int(content)
            return self.getMoney(member,content)

    def updateLevel(self,member):
        userId = getPerson(member).userId
        coin = getCoin(userId)
        temp = self.dao.selectByUserId(userId)
        if(temp[4] == 1):
            if(coin<4000):
                return "银牌会员需要4000大给币！"
            saveCoin(-4000,userId)
            self.dao.updateLevel(userId,4000)
            return "已提升为银牌会员"
        if(temp[4] == 2):
            if(coin<10000):
                return "金牌会员需要10000大给币！"
            saveCoin(-10000,userId)
            self.dao.updateLevel(userId,10000)
            return "已提升为金牌会员"
        if(temp[4] == 3):
            return "已经达到最大会员等级！"


    def openBank(self,member):
        userId = getPerson(member).userId
        coin = getCoin(userId)
        if(coin<200):
            return "开户需要200大给币！"
        self.dao.insert(userId)
        saveCoin(-200,userId)
        return "开户成功 输入 [银行信息] 查看"

    def showBankInfo(self,member):
        self.result = "欧尼酱的银行信息如下：\n"
        temp = self.dao.selectByUserId(getPerson(member).userId)
        if(temp == None):
            return "未开户，去[开户]吧"
        self.result += "现有存款:"+str(temp[2])+" 最大存款:"+str(temp[3])+" 银行会员等级:"+str(temp[4])+"\n"
        self.result += "去[存钱]吧！"
        return self.result

    def saveMoney(self,member,content):
        userId = getPerson(member).userId
        temp = self.dao.selectByUserId(userId)
        if(int(temp[2])+int(content)>int(temp[3])):
            return "超过最大存款额，去[提升银行会员]等级吧！"
        saveCoin(-content,userId)
        self.dao.updateMoney(userId,content)
        return "存款成功！存入"+str(content)

    def getMoney(self,member,content):
        userId = getPerson(member).userId
        temp = self.dao.selectByUserId(userId)
        if(temp[2]<content):
            return "没有那么多大给币"
        saveCoin(content,userId)
        self.dao.updateMoney(userId,-content)
        return "取款成功！取出"+str(content)
