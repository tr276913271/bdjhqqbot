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
        self.userId = tuple[9]
        self.maxhp = tuple[10]
        self.profession = CodeDBService.CodeDB['职业类型'][self.profession-1]

    def attack(self):
        return self.weapon.atk

    def defensive(self):
        return self.head.defs+self.breast.defs

    def level(self):
        return self.level

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

    def handAfterBattle(self,pa,pb):
        result=""
        aexp = 0
        if(pb.hp<0):
            pb.hp = 0
            aexp += math.floor(40*round(1+random.uniform(-0.1,0.1),2))
        aexp += math.floor(10*round(1+random.uniform(-0.1,0.1),2))
        pa.exp += aexp
        result += pa.name + " 获得"+str(aexp)+"点经验\n"
        if(pa.exp/100 > pa.level):
            result += pa.name + "升级了！！\n"
            pa.level+=1
            pa.exp-=100
            pa.maxhp += 100
        return result

    def battleWith(self,user):
        result,flag = BattleProcess().battleWith(self,user)
        if(flag):
            result += self.handAfterBattle(self,user)
            result += self.handAfterBattle(user,self)
        return result,flag

class BattleProcess:
    def damage(self,a,b):
        flag = False
        damage =  math.floor(a.attack()*round(1+random.uniform(-0.1,0.2),2))-b.defensive()
        if(random.randint(1,10)<=2):
            damage = 2*damage
            flag = True
        return damage, flag

    def oneRound(self,a,b,flag):
        damage, crit = self.damage(a,b)
        b.hp = b.hp-damage
        if(flag):
            if(crit):
                self.result += "我方暴击伤害:"+str(damage)+",对方当前HP:"+str(b.hp)
            else:
                self.result += "我方伤害:"+str(damage)+",对方当前HP:"+str(b.hp)
        else:
            if(crit):
                self.result += "对方暴击伤害:"+str(damage)+",我方当前HP:"+str(b.hp)
            else:
                self.result += "对方伤害:"+str(damage)+",我方当前HP:"+str(b.hp)

    def battleWith(self,a,b):
        self.result = a.name + " HP:"+str(a.hp)+" ATK:"+str(a.attack())+" DEF:"+str(a.defensive())+" vs "
        self.result += b.name + " HP:"+str(b.hp)+" ATK:"+str(a.attack())+" DEF:"+str(b.defensive())+"\n"
        if(b.hp<=0):
            return "对方HP：0 对方濒死，君子不乘人之危\n",False
        if(a.hp<=0):
            return "我方HP：0 你就是个弟弟啊，不要去招惹他人\n",False
        if(b.defensive()>=a.attack()):
            return "对方DEF："+str(b.defensive())+" 我方ATK："+str(a.attack())+"\n 你就是个弟弟啊，不要去招惹他人",False
        for i in range(5):
            self.result += "第"+str(i+1)+"轮："
            self.oneRound(a,b,True)
            if(b.hp<=0):
                return self.result+"\n"+a.name+" 战胜了 "+b.name+"\n",True
            self.result += " "
            self.oneRound(b,a,False)
            if(a.hp<=0):
                return self.result+"\n"+b.name+" 战胜了 "+a.name+"\n",True
            self.result += "\n"
        return self.result+"平手\n",True
