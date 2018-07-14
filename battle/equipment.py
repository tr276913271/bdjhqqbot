# -*- coding: UTF-8 -*-

class Equipment:
    def __init__(self,name,type,id,atk,defs):
        self.name = name
        self.type = type
        self.id = id
        self.atk = atk
        self.defs = defs

    def initPerson(p):
        p.weapon = Equipment("破旧的剑",2,2,10,0)
        p.head = Equipment("新手头盔",1,1,0,10)
        p.breast = Equipment("新手胸甲",3,3,0,10)

    def showInfo(self):
        return self.name+" ATK:"+str(self.atk)+" DEF:"+str(self.defs)
