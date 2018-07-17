# -*- coding: UTF-8 -*-
from battle_module import *
from db_module.code_db import CodeDBService
import json,math,random


class Person:
    def __init__(self,name):
        self.name = name
        self.weapon = None
        self.head = None
        self.breast = None
        self.hp = 1000
        self.maxhp = 1000
        self.level = 1
        self.exp = 1
        self.profession = 1
        equipment_db.EquipmentDB.initPerson(self)

    def initWithDB(self,tuple):
        self.weapon = equipment_db.EquipmentDB.EDB[tuple[8]]
        self.head = equipment_db.EquipmentDB.EDB[tuple[6]]
        self.breast = equipment_db.EquipmentDB.EDB[tuple[7]]
        self.hp = tuple[2]
        self.level = tuple[1]
        self.exp = tuple[3]
        self.id = tuple[0]
        self.maxhp = tuple[10]
        self.profession = CodeDBService.CodeDB['职业类型'][self.profession-1]

    def attack(self):
        return self.weapon.atk

    def defensive(self):
        return self.head.defs+self.breast.defs

    def level(self):
        return self.exp/100

    def showInfo(self):
        info = "欧尼酱的人物信息如下哦：\n"
        info += "ID："+self.name+" "+"MAXHP/HP："+str(self.maxhp)+"/"+str(self.hp)+"\n"
        info += "职业："+str(self.profession.codeName)+"\n"
        info += "等级："+str(self.level)+"\n"
        info += "经验："+str(self.exp)+"\n"
        info += "攻击力："+str(self.attack())+"\n"
        info += "防御力："+str(self.defensive())+"\n"
        info += "头部："+self.head.showInfo()+"\n"
        info += "胸部："+self.breast.showInfo()+"\n"
        info += "武器："+self.weapon.showInfo()+"\n"
        return info

    def obj_2_json(self):
        return json.dumps(self,default=lambda obj: obj.__dict__,ensure_ascii=False)

    def battleWith(self,userId):
        return BattleProcess().battleWith(self,userId)

class BattleProcess:
    def damage(self,a):
        flag = False
        damage =  math.floor(a.attack()*round(1+random.uniform(-0.2,0.2),2))
        if(random.randint(1,10)<=2):
            damage = 2*damage
            flag = True
        return damage, flag

    def oneRound(self,a,b,flag):
        catk, crit = self.damage(a)
        cdef = b.defensive()
        b.hp = b.hp-(catk-cdef)
        if(flag):
            if(crit):
                self.result += "我方造成暴击伤害:"+str(catk-cdef)+",对方当前HP:"+str(b.hp)+"\n"
            else:
                self.result += "我方造成伤害:"+str(catk-cdef)+",对方当前HP:"+str(b.hp)+"\n"
        else:
            if(crit):
                self.result += "对方造成暴击伤害:"+str(catk-cdef)+",我方当前HP:"+str(b.hp)+"\n"
            else:
                self.result += "对方造成伤害:"+str(catk-cdef)+",我方当前HP:"+str(b.hp)+"\n"

    def battleWith(self,a,b):
        self.result = a.name + " HP:"+str(a.hp)+" ATK:"+str(a.attack())+" DEF:"+str(a.defensive())+"\n"
        self.result += b.name + " HP:"+str(b.hp)+" ATK:"+str(a.attack())+" DEF:"+str(b.defensive())+"\n"
        if(b.hp<=0):
            return "对方HP：0 对方濒死，君子不乘人之危\n"
        if(a.hp<=0):
            return "我方HP：0 你就是个弟弟啊，不要去招惹他人\n"
        if(b.defensive()>=a.attack()):
            return "对方DEF："+str(b.defensive())+" 我方ATK："+str(a.attack())+"\n"
        for i in range(3):
            self.oneRound(a,b,True)
            if(b.hp<=0):
                return self.result+a.name+" 战胜了 "+b.name+"\n"
            self.oneRound(b,a,False)
            if(a.hp<=0):
                return self.result+b.name+" 战胜了 "+a.name+"\n"
        return self.result
