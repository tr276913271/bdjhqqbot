# -*- coding: UTF-8 -*-

class Equipment:
    def __init__(self,tuple):
        self.id = tuple[0]
        self.desc = tuple[1]
        self.name = tuple[2]
        self.type = tuple[3]
        self.atk = tuple[4]
        self.defs = tuple[5]

    def initPerson(p):
        p.weapon = Equipment("破旧的剑",2,2,10,0)
        p.head = Equipment("新手头盔",1,1,0,10)
        p.breast = Equipment("新手胸甲",3,3,0,10)

    def showInfo(self):
        return self.name+" ATK:"+str(self.atk)+" DEF:"+str(self.defs)
