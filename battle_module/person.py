# -*- coding: UTF-8 -*-
from battle_module import *
from db_module.code_db import CodeDBService
import json

class Person:
    def __init__(self,name):
        self.name = name
        self.weapon = None
        self.head = None
        self.breast = None
        self.hp = 100
        self.maxhp = 100
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

if __name__ == '__main__':
    p = Person("kgm")
    print(p.showInfo())
