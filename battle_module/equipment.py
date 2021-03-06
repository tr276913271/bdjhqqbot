# -*- coding: UTF-8 -*-
import math

class Equipment:
    def __init__(self,tuple):
        self.id = tuple[0]
        self.desc = tuple[1]
        self.name = tuple[2]
        self.type = tuple[3]
        self.atk = tuple[4]
        self.defs = tuple[5]
        self.price = tuple[7]
        self.etype = tuple[6]
        self.probability = tuple[8]
    def showInfo(self):
        return self.name+" ATK:"+str(self.atk)+" DEF:"+str(self.defs)

    def __repr__(self):
        return self.showDetaiInfo()

    def showDetaiInfo(self):
        result = "ID:"+str(self.id)+" 价格："+str(self.price)+" 大给币\n"
        result += self.name+" ATK:"+str(self.atk)+" DEF:"+str(self.defs)+'\n'
        if(self.desc == None):
            self.desc = ""
        result += "描述："+self.desc+'\n'
        result += '=================\n'
        return result

    def showPackageInfo(self):
        result = "ID:"+str(self.id) +" "+ self.name +" 卖价："+str(self.sellPrice())+" \n"
        return result

    def sellPrice(self):
        return math.floor(self.price/3)
