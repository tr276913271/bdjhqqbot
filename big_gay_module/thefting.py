#- * -coding: utf - 8 - * -
from big_gay_module.theftSys import TheftSystem
class TheSteal:
    def stealing(self, content):
        if content.find('偷窃@') == 1 :
            return True
        else：
            return False
    
    def stealingFun(self, member, content):
        #member1偷窃者 member2被偷窃者
        self.member1 = member
        self.member2 = content.strip('偷窃@')
        #判断两方是否存在
        if len(DBHelper().selectAll("select name from theft where name = '"+str(self.member1)+"' ")) == 0:
            self.mensrt = self.member1''
            return 


        self.member2 = (self.member2).strip(' ')
        self.mensrt = TheftSystem().theftFun(member1, member2)
        return self.mensrt

        


