#- * -coding: utf - 8 - * -
import random

class SignInRoll:
    rollListSet = False
    def signRollIfSet(self,member):
        if member != '铁花':
            menstr = '需要管理员创建ROLL点表'
        else:
            rollListSet = True
            rollList = {}
            menstr = '已创建列表'
        return menstr
    
    def signInRollIf(self,content):
        if content.find('创建列表') >= 0:
            return True
        else:
            return False
    
    def enrollIf(self,content):
        if content.find('报名') >= 0 :
            return True
        else:
            return False

    def enroll(self,member):
        if rollListSet = True and member not in self.rollList :
            rollValue = random.randint(1,100)
            self.rollList[member]=rollValue
            return '报名成功'
        else:
            return '重复报名了'

    def judgmentif(self,member,contet):
        if member = '铁花' and content.find('roll点开始'):
            return True
        else:
            return False
    
    def judgment(self):
        maxRoll = 0
        maxName = ''
        menstr = ''
        rollListSet = False
        for key,value in self.rollList.iteritems():
            menstr += key + 'ROLL了' + self.rollList + '点 \n'
            if rollList[key] > maxRoll:
                maxRoll = rollList[key]
                maxName = key
            menstr += '胜利者是' + maxName + 'ROll了' + maxRoll + '点'
        return menstr
        
