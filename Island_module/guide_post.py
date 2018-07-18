# -*- coding: UTF-8 -*-
from db_module.data_tuple_to_str import DBTStr

class GuidePost:
    def commonPostOne(self, content):
        content = content.strip('常用串：')
        content = content.strip(' ')
        menstr = DBTStr().thePostOne(content)
        return menstr


    #判断
    def commonPostIf(self, content):
        if content.find('常用串') >= 0:
            return True
        else:
            return False

    #分类
    def commonPostIfFun(self,content):
        if content.find('常用串：') >= 0:
            menstr = self.commonPostOne(content)
            return menstr
        elif content.find('常用串') >= 0:
            menstr = '功能未添加'
            return menstr
        else:
            menstr = '使用正确格式就能查找常用串咯哦~'
            return menstr
