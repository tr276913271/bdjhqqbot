# -*- coding: UTF-8 -*-
class InstructionsIntroduce:
    def orderIntroduce(self):
        menstr = "名称：效果\n"
        menstr += "鸡盒：领鸡盒 hp+1000\n"
        menstr += "偷窃：偷窃@姓名\n"
        menstr += "商店武器：\n"
        menstr += "商店头盔：\n"
        menstr += "商店胸甲：\n"
        menstr += "买药：20大给币 HP回满\n"
        menstr += "喂饼：喂饼@姓名 20大给币 给对方回满血\n"
        menstr += "挑战：挑战世界BOSS\n"
        menstr += "人物信息：查看面板\n"
        menstr += "世界首领：世界BOSS信息\n"
        menstr += "大给币：打卡领币\n"
        menstr += "查询：查询有多少大给币\n"
        menstr += "求组队：打本组队\n"
        menstr += "半姬私语：公告板\n"
        menstr += "下版本玩什么：ROLL职业\n"
        menstr += "ROLL：ROLL点\n"
        menstr += "决斗：决斗@姓名 干死别人\n"
        menstr += "背包：查看背包信息\n"
        menstr += "卖出[ID]：卖出装备\n"
        menstr += "装备[ID]：装备装备\n"
        return menstr

    def instructionsIf(self,content):
        if content == '指令':
            return True
        else:
            return False

