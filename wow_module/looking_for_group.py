#- * -coding: utf - 8 - * -
import  time

class LookingForGroupService:
    #类变量，可以认为是静态变量
    ticks = 0
    groupMember = set([])
    def shouldService(self,member,content):
        if(content=='求组队'):
            if(int(time.time())>LookingForGroupService.ticks):
                LookingForGroupService.groupMember.clear()
                LookingForGroupService.ticks = int(time.time())+600
            LookingForGroupService.groupMember.add(member)
            return True
        return False

    def service(self,member):
        s=""
        if(len(LookingForGroupService.groupMember)<4):
            s = "欧尼酱，快来打本呀 |-` )，现在只有：\n"
        else:
            s = "欧尼酱，人很多了呀，可以开始打本了(＾o＾)ﾉ，现在有：\n"
        return self.handleReturn(s)

    def handleReturn(self,s):
        for m in LookingForGroupService.groupMember:
            s +=  m+" 大佬 \n"
        return s
