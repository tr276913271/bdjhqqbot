# -*- coding: UTF-8 -*-

class Equipment:
    def __init__(self,tuple):
        self.id = tuple[0]
        self.desc = tuple[1]
        self.name = tuple[2]
        self.type = tuple[3]
        self.atk = tuple[4]
        self.defs = tuple[5]
    def showInfo(self):
        return self.name+" ATK:"+str(self.atk)+" DEF:"+str(self.defs)
