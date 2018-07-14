# -*- coding: utf-8 -*-
import random

class WowPlayService:
    def shouldService(self,content):
        if (content.find('8.0玩什么') >= 0):
            return True
        elif (content.find('下版本玩什么') >= 0):
            return True
        else:
            return False

    def service(self):
        professionList = self.initProfessionList()
        r = random.randint(0,120);
        resultStr = "(　^ω^)欧尼酱roll的点数为:"+str(r)+"\n"
        resultStr += "下个版本推荐玩:\n"
        resultStr += professionList[r%12]+"\n"
        return resultStr

    def initProfessionList(self):
        professionList = []
        professionList.append('''
        糖门滚\n
        糖门滚？不存在的！8.0术士获得了巨大BUFF，马桶和门都获取的全新的超酷外观！每个BOSS都可以拉一个糖门，不用滚了！
        ''')
        professionList.append('''
        狗的主人\n
        下个版本还有大米，射击猎无敌呀，一箭射出去整个副本的怪都能受到伤害，太IMBA了！
        ''')
        professionList.append('''
        furry\n
        毛茸茸的熊，可以（被）骑的鹿，WOW第一吉祥物咕咕！这么多理由还不值得练吗？
        ''')
        professionList.append('''
        渡鸦\n
        对，就是那个能够变成卡神棍还能放三分归元气的那只渡鸦！
        ''')
        professionList.append('''
        狂暴武器战\n
        安度因狂暴武器战！还带群体治疗，群体复活，还送个能够让你看起来很MAN的面具。
        ''')
        professionList.append('''
        没有刺杀贼了\n
        7.0被盗贼恶心够了没，告诉你下版本他还是这么恶心，不想被恶心就练一个恶心别人去！
        ''')
        professionList.append('''
        ATM\n
        移动荣誉，强无敌，特效最酷炫，打不过不怕，我们最拉风啊！
        ''')
        professionList.append('''
        圣光啊\n
        想赣骚蹄子伊瑞尔吗！起个圣骑加入圣光啊！
        ''')
        professionList.append('''
        冲钅\n
        瓦王都被古尔丹射爆了，不起个战士去复仇？忍心吗？你还是联盟的一份子吗？
        ''')
        professionList.append('''
        瘸子\n
        瞎子都洗白了，瘸子洗白也是早晚的事，况且瘸子这么屌，不练一个吗？
        ''')
        professionList.append('''
        秃子\n
        肝了整个7.0还能不秃吗？快加入五晨寺吧，大家一起秃秃的。
        ''')
        professionList.append('''
        瞎子\n
        电子竞技不需要视力。欲练竞技，引刀自宫。
        ''')
        return professionList
