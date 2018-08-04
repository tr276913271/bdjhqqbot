#- * -coding: utf - 8 - * -
from db_module.connect_db import DBHelper
import time, datetime

class NgaQuest():
    def ngaFixQAIfFix(self,content):
        if content.find('热修') >= 0:
            menstr = self.ngaHotFix()
            return menstr
        elif content.find('近期更新') >= 0:
            menstr = self.ngaRecentFix()
            return menstr
        else:
            menstr = self.ngaFixQA()
            return menstr


    def ngaFixQAIf(self,content):
        if content.find('热修') >= 0:
            return True
        elif content.find('今日WOW') >= 0:
            return True
        elif content.find('今日wow') >= 0:
            return True
        elif content.find('今天wow') >= 0:
            return True
        elif content.find('今天WOW') >= 0:
            return True
        elif content.find('wow更新') >= 0:
            return True
        elif content.find('WOW更新') >= 0:
            return True
        elif content.find('近期更新') >=0:
            return True
        else:
            return False
    
    def ngaFixQA(self):
        todayTime = time.strftime("%Y-%m-%d", time.localtime())
        menstr = DBHelper().selectAll("select potitle, superlink from nga where  date_format(posttime, '%Y-%m-%d') = '"+todayTime+"' and poid != '1'")
        if len(menstr) == 0:
            result = "今天阿三没上班，还没有任何更新喔~"
        else:
            result = ""
            for t in menstr:
                result += t[0]+":"+t[1]+"\n"
        return result

    def ngaHotFix(self):
        todayTime = time.strftime("%Y-%m-%d", time.localtime())
        menstr = DBHelper().selectAll("select potitle, superlink from nga where  date_format(posttime, '%Y-%m-%d') = '"+todayTime+"' and potitle like '%修正%'")
        if len(menstr) == 0:
            result = "今天阿三没上班，没有热修，日常阅读在线修正任务（0/1）"
        else:
            result = ""
            for t in menstr:
                result += t[0]+":"+t[1]+"\n"
        return result

    def ngaRecentFix(self):
        todayTime = time.strftime("%Y-%m-%d", time.localtime())
        todayTimedata = datetime.datetime.strptime(todayTime,"%Y-%m-%d")
        de = datetime.timedelta(days = 3)
        todayTimedata = todayTimedata - de
        recentTime = datetime.datetime.strftime(todayTimedata,"%Y-%m-%d")
        menstr = DBHelper().selectAll("select potitle, superlink from nga where  date_format(posttime, '%Y-%m-%d') > '"+recentTime+"' and poid != '1'")
        if len(menstr) == 0:
            result = "阿三三天没上班了也，还不更新！"
        else:
            result = ""
            for t in menstr:
                result += t[0]+":"+t[1]+"\n"
        return result


