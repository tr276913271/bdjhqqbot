#- * -coding: utf - 8 - * -
from big_gay_module.theftSys import TheftSystem
from db_module.like_member import LikeMember
from db_module.connect_db import DBHelper
from db_module.data_tuple_to_str import DBTStr

class TheSteal:
    def stealing(self, content):
        if content.find('偷窃@') >= 0 :
            return True
        else:
            return False
    
    def stealingFun(self, member, content):
        #member1偷窃者 member2被偷窃者
        self.member1 = member
        content = content.strip('偷窃@')
        self.member2 = content.strip('')
        #self.member2 = LikeMember().likeMember(self.member2)
        #判断两方是否存在
        if LikeMember().likeMemberBe(self.member1) == False:
            self.menstr = self.member1 + '欧尼酱你还没有领取过大给币哦~请先领取了才能偷别人的！'
            return self.menstr
        elif LikeMember().likeMemberBe(self.member2) == False:
            self.menstr = self.member1 + '欧尼酱你偷取的对象没有领取过大给币哦~'
            return self.menstr
        else:
            self.member2 = LikeMember().likeMember(self.member2)
            # 查询次数member1当天的偷取的次数
            if int( DBTStr().theftNum(self.member1)) < 3:
                # 查询member2当天被偷窃的次数
                if int ( DBTStr().theBeFtNum(self.member2)) <3:
                    self.member2 = LikeMember().likeMember(self.member2)
                    self.menstr = TheftSystem().theftFun(self.member1, self.member2)
                    return self.menstr
                else:
                    self.menstr = self.member2 + '欧尼酱今天被偷过3次了哦，他提高戒心了呢，偷不到了(つд⊂)'
                    return self.menstr
            else:
                self.menstr = self.member1 + '欧尼酱你今天已经偷过3次了，还这么贪心的吗！小心扣你大给币！(￣︿￣)'
                return self.menstr



        #self.member2 = (self.member2).strip(' ')
        #self.mensrt = TheftSystem().theftFun(member1, member2)
        #return self.mensrt

        


