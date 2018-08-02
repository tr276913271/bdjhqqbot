# -*- coding: UTF-8 -*-
from battle_module import *
from db_module.connect_db import DBHelper
from battle_module.battle_util import *

class WeaponDao:
    def __init__(self):
        self.db = DBHelper()

    def selectByType(self,type):
        result = []
        for e in equipment_db.EquipmentDB.EDB:
            if(equipment_db.EquipmentDB.EDB[e].type == type and equipment_db.EquipmentDB.EDB[e].etype ==1):
                result.append(equipment_db.EquipmentDB.EDB[e])
        return result

    def selectBasicUser(self,member):
        print(member)
        userId = battle_service.BattleDao().selectUid(member)
        p = person.Person(member)
        p.initBasicWithDB(self.db.selectOne("select * from battle where userId="+str(userId[0])))
        return p

    def updateEquipInfo(self,p):
        self.db.update("update battle set head="+str(p.head)+" ,body = "+str(p.breast)+",weapon = "+str(p.weapon)+" where userId="+str(p.userId))

    def addPackage(self,userId,equipId):
        self.db.update("insert package (userId,equipId) VALUES ("+str(userId)+","+str(equipId)+")")

class WeaponService:
    def __init__(self):
        self.result = ""
        self.battleService = battle_service.BattleService()

    def shouldService(self,content):
        if(content=='商店武器'):
            return True
        if(content=='商店头盔'):
            return True
        if(content=='商店胸甲'):
            return True
        if(content.find('购买') >= 0):
            content = content.strip('购买')
            flag,eid = battle_util.strToInt(content)
            return flag
        if(content=='背包'):
            return True
        if(content.find('卖出') >= 0):
            content = content.strip('卖出')
            flag,eid = battle_util.strToInt(content)
            return flag
        if(content.find('装备') >= 0):
            content = content.strip('装备')
            flag,eid = battle_util.strToInt(content)
            return flag
        return False

    def service(self,member,content):
        if(content=='商店武器'):
            return self.showWeaponInfo(2)
        if(content=='商店头盔'):
            return self.showWeaponInfo(1)
        if(content=='商店胸甲'):
            return self.showWeaponInfo(3)
        if(content.find('购买') >= 0):
            self.battleService.register(member)
            content = content.strip('购买')
            eid = int(content)
            return self.buy(member,eid)
        if(content=='背包'):
            self.battleService.register(member)
            return self.showPackage(member)
        if(content.find('卖出') >= 0):
            self.battleService.register(member)
            content = content.strip('卖出')
            eid = int(content)
            return self.sellPackage(member,eid)
        if(content.find('装备') >= 0):
            self.battleService.register(member)
            content = content.strip('装备')
            eid = int(content)
            return self.equipEquipment(member,eid)
        return "a"

    def equipEquipment(self,member,eid):
        wdao = WeaponDao()
        p = wdao.selectBasicUser(member)
        plist = package_dao.PackageDao().selectByUserIdAndEquipId(p.userId,eid)
        for e in plist:
            if(e[2]==eid):
                ee = equipment_db.EquipmentDB.EDB[e[2]]
                if(ee.type==1):
                    p.head = ee.id
                if(ee.type==2):
                    p.weapon = ee.id
                if(ee.type==3):
                    p.body = ee.id
                wdao.updateEquipInfo(p)
                return "已装备"+ee.name+" 输入 人物信息 查看"
        return "没有这件装备哦，去商店看看吧"

    def sellPackage(self,member,eid):
        wdao = WeaponDao()
        p = wdao.selectBasicUser(member)
        pDao = package_dao.PackageDao()
        dao = battle_service.BattleDao()
        plist = pDao.selectByUserIdAndEquipId(p.userId,eid)
        if(p.head==eid or p.weapon==eid or p.breast==eid):
            return "穿在身上的装备不能卖哦，输入 装备[编号] 换装备"
        price = 0
        for e in plist:
            price += equipment_db.EquipmentDB.EDB[e[2]].sellPrice()
        pDao.sellByUserIdAndEquipId(p.userId,eid)
        dao.updateCoin(price,p.userId)
        return "卖出了"+str(price)+" 大给币"

    def showPackage(self,member):
        wdao = WeaponDao()
        pDao = package_dao.PackageDao()
        p = wdao.selectBasicUser(member)
        plist = pDao.select(p.userId)
        result = ""
        for e in plist:
            result += str(equipment_db.EquipmentDB.EDB[e[2]].showPackageInfo())
        return result

    def buy(self,member,eid):
        wdao = WeaponDao()
        p = wdao.selectBasicUser(member)

        dao = battle_service.BattleDao()
        coin = dao.selectCoin(p.userId)

        if(eid > len(equipment_db.EquipmentDB.EDB)):
            return "不存在的装备"
        e = equipment_db.EquipmentDB.EDB[eid]
        if(e.etype == 2):
            return "不存在的装备哦"
        if(coin[0] < e.price):
            return "大给币不够哦，打卡，任务，偷窃，都可以增加大给币哦"
        if(e.type == 1):
            p.head = e.id
        if(e.type == 2):
            p.weapon = e.id
        if(e.type == 3):
            p.breast = e.id
        wdao.updateEquipInfo(p)
        wdao.addPackage(p.userId,e.id)
        dao.updateCoin(-e.price,p.userId)
        return "购买成功，输入 人物信息 查看欧尼酱现在的属性面板吧"

    def showWeaponInfo(self,type):
        list = WeaponDao().selectByType(type)
        for e in list:
         self.result += e.showDetaiInfo()
        return self.result
