#- * -coding: utf - 8 - * -
from big_gay_module.theftSys import TheftSystem
class TheSteal:
    def stealing(self, member, content):
        #member1偷窃者 member2被偷窃者
        self.member1 = member
        self.member2 = content.strip('偷窃@')
        self.member2 = (self.member2).strip(' ')
        self.mensrt = TheftSystem().theftFun(member1, member2)
        return self.mensrt


