# -*- coding: UTF-8 -*-
from equipment import Equipment
from equipment_db import EquipmentDB
import json

class Person:
    def __init__(self,name):
        self.name = name
        self.weapon = None
        self.head = None
        self.breast = None
        self.hp = 100
        self.level = 1
        self.exp = 1
        Equipment.initPerson(self)

    def attack(self):
        return self.weapon.atk

    def defensive(self):
        return self.head.defs+self.breast.defs

    def level(self):
        return self.exp/100

    def showInfo(self):
        info = "欧尼酱的人物信息如下哦：\n"
        info += "ID："+self.name+"\n"
        info += "HP："+str(self.hp)+"\n"
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
