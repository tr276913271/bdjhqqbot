#- * -coding: utf - 8 - * -
import random
#rollListSet = False
#rollList = {}
rollListSet = False
rollList = {}
class SignInRoll:
    #rollListSet = False
    def signRollIfSet(self,member):
        if member != '只是一只孤狼的' :
            menstr = '需要管理员创建ROLL点表'
        else:
            global rollListSet
            rollListSet = True
            #rollList = {}
            menstr = '已创建列表'
        return menstr
    
    def signInRollIf(self,content):
        if content.find('创建ROLL卡活动') >= 0:
            return True
        else:
            return False
    
    def enrollIf(self,content):
        if content.find('给我也来一个') >= 0 :
            return True
        else:
            return False

    def enroll(self,member):
        global rollList
        if rollListSet == True and member not in rollList :
            rollValue = random.randint(1,100)
            rollList[member]=rollValue
            return '参与成功了'
        else:
            return '重复报名或者还没开启活动呢'

    def judgmentif(self,member,content):
        if member == '只是一只孤狼的' and content.find('活动开始！') >= 0 :
            return True
        else:
            return False
    
    def judgment(self):
        maxRoll = 0
        maxName = ''
        menstr = ''
        global rollListSet
        global rollList
        rollListSet = False
        for key,value in rollList.items():
            menstr += key + 'ROLL了' + str(value) + '点 \n'
            if rollList[key] > maxRoll:
                maxRoll = rollList[key]
                maxName = key
        menstr += '胜利者是' + maxName + 'ROll了' + str(maxRoll) + '点'
        rollList.clear()
        return menstr
        
