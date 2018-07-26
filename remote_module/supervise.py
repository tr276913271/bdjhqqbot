#- * -coding: utf - 8 - * -
from db_module.connect_db import DBHelper
import threading

class AdminSupervise:
    def administrator (self, member):
        if member == '铜壶煮三江':
            return True
        elif member =='铁花':
            return True
        elif member =='姬小路':
            return True
        else:
            return False

#    def turnOff(self,content):
#        if self.administrator(member):
#            if content == '半姬睡觉吧':
#                menstr = '好的，睡了'
#                bot.Stop()
#                return menstr
#        else :
#            return False

    # 远程插入数据库方法
    def remotdbc(content):
        content = content.strip('数据库插入')
        DBHelper().insert('+content+')

    #远程关机延时任务
    #def sleepShutdown(self):
    #    bot.stop()
    #    t = threading.Timer(20,sleepShutdown)
    #    t.start()



    #远程方法判断
    def remoteAdminService(self,content):
        if content.find('数据库插入') >= 0 :
            self.remotdbc(content)
            memstr = '数据库已更新'
            return memstr
        #elif content == '你该睡觉了':
        #    memstr = '好的，我去睡觉啦'
        #    self.sleepShutdown()
        #    return memstr
        else:
            memstr = '暂时还没有这个功能'
            return memstr




