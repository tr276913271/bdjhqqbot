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
        self.atk = tuple[4]
        self.defense = tuple[5]
        self.userId = tuple[9]
        self.maxhp = tuple[10]
        self.profession = CodeDBService.CodeDB['职业类型'][tuple[11]-1]

    def initBasicWithDB(self,tuple):
        self.weapon = tuple[8]
        self.head = tuple[6]
        self.breast = tuple[7]
        self.hp = tuple[2]
        self.level = tuple[1]
        self.exp = tuple[3]
        self.atk = tuple[4]
        self.defense = tuple[5]
        self.userId = tuple[9]
        self.maxhp = tuple[10]
        self.profession = tuple[11]

    def attack(self):
        return self.weapon.atk+self.atk

    def defensive(self):
        return self.head.defs+self.breast.defs+self.defense

    def level(self):
        return self.level

    def showInfo(self):
        info = "欧尼酱的人物信息如下哦：\n"
        info += "ID："+self.name+" "+"MAXHP/HP："+str(self.maxhp)+"/"+str(self.hp)+"\n"
        info += "职业："+str(self.profession.codeName)+"\n"
        info += "等级："+str(self.level)+"\n"
        info += "经验："+str(self.exp)+"\n"
        info += "力量："+str(self.atk)+"  敏捷："+str(self.defense)+"\n"
        info += "攻击力："+str(self.attack())+"\n"
        info += "防御力："+str(self.defensive())+"\n"
        info += "头部："+self.head.showInfo()+"\n"
        info += "胸部："+self.breast.showInfo()+"\n"
        info += "武器："+self.weapon.showInfo()+"\n"
        return info

    def obj_2_json(self):
        return json.dumps(self,default=lambda obj: obj.__dict__,ensure_ascii=False)


    def battleWith(self,user):
        process = BattleProcess()
        flag = process.battleWith(self,user)
        if(flag):
            process.handleAfterBattle(self,user)
            process.handleAfterBattle(user,self)
        return process.result,flag,process

class BattleProcess:
    hobby = ['足控','奶子','屁股','Furry','萝莉控']
    def __init__(self):
        self.aAttackCount = 0
        self.bAttackCount = 0
        self.aDamage = 0
        self.bDamage = 0
        self.bCritCount = 0
        self.aCritCount = 0

    def damage(self,a,b,times=1):
        flag = False
        damage =  math.floor(a.attack()*times*round(1+random.uniform(-0.1,0.2),2))-b.defensive()
        if(damage<0):
            damage = 0
        if(random.randint(1,10)<=2):
            damage = 2*damage
            flag = True
        return damage, flag

    def oneRound(self,a,b,flag,times=1):
        damage, crit = self.damage(a,b,times)
        if(flag):
            if(crit):
                self.aCritCount += 1
            else:
                self.aAttackCount += 1
            self.aDamage += damage
        else:
            if(crit):
                self.bCritCount += 1
            else:
                self.bAttackCount += 1
            self.bDamage += damage
        return damage


    def handleMessage(self,a,b):
        self.result +="本次战斗："+ a.name +" 造成了:"+str(self.aDamage) +"点伤害 "+ " 普攻次数:"+str(self.aAttackCount)+" 暴击次数:"+str(self.aCritCount)+"\n"
        self.result +="本次战斗："+ b.name +" 造成了:"+str(self.bDamage) +"点伤害 "+ " 普攻次数:"+str(self.bAttackCount)+" 暴击次数:"+str(self.bCritCount)+"\n"

    def battleWith(self,a,b):
        self.result = a.name + " HP:"+str(a.hp)+" ATK:"+str(a.attack())+" DEF:"+str(a.defensive())+" vs "
        self.result += b.name + " HP:"+str(b.hp)+" ATK:"+str(b.attack())+" DEF:"+str(b.defensive())+"\n"
        if(b.hp<=0):
            self.result = "对方HP：0 对方濒死，趁热……快……趁热\n"
            return False
        if(a.hp<=0):
            self.result =  "我方HP：0 我方濒死，难道你想被趁热吗……\n"
            return False
        if(b.defensive()>=a.attack()):
            self.result =  "对方DEF："+str(b.defensive())+" 我方ATK："+str(a.attack())+"\n 你就是个弟弟啊，不要去招惹他人"
            return False
        for i in range(30):
            b.hp -= self.oneRound(a,b,True)
            if(b.hp<=0):
                self.result += "\n"+a.name+" 战胜了 "+b.name+"!\n"
                self.deathBattle(b,a)
                self.handleMessage(a,b)
                return True
            a.hp -= self.oneRound(b,a,False)
            if(a.hp<=0):
                self.result += "\n"+b.name+" 战胜了 "+a.name+"!\n"
                self.deathBattle(a,b)
                self.handleMessage(a,b)
                return True

        self.handleMessage(a,b)
        self.result+="平手\n"
        return True
#破釜沉舟
    def deathBattle(self,a,b):
        if(random.randint(0,100)>30):
            return ""
        self.result += a.name +"濒死\n但由于"+random.sample(BattleProcess.hobby, 1)[0]+"之神的眷顾，他发动了[破釜沉舟]，攻击力翻倍！\n"
        a.hp = a.maxhp/3
        for i in range(30):
            b.hp -= self.oneRound(a,b,True,2)
            if(b.hp<=0):
                self.result += "张狂的"+b.name + " 被击败了！\n"
                return
            a.hp -= self.oneRound(b,a,False)
            if(a.hp<=0):
                self.result += "可怜的"+a.name + "还是失败了！\n"
                return
        self.result += "平手\n"
        return


    def handleAfterBattle(self,pa,pb):
        aexp = 0
        if(pb.hp<0):
            pb.hp = 0
            factor = pb.level/pa.level
            if(factor>5):
                factor = 5
            elif(factor<0):
                factor = 0
            aexp += math.floor(40*round(1+random.uniform(-0.1,0.1),2)*(factor))
        aexp += math.floor(10*round(1+random.uniform(-0.1,0.1),2))
        pa.exp += aexp
        self.result += pa.name + " 获得"+str(aexp)+"点经验\n"
        while(pa.exp/100 > pa.level):
            self.result += pa.name + "升级了！！\n"
            pa.level+=1
            pa.maxhp += 100
            pa.hp += 1000
            if(pa.hp>=pa.maxhp):
                pa.hp = pa.maxhp
