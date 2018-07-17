#- * -coding: utf - 8 - * -
from db_module.connect_db import DBHelper
from db_module.data_tuple_to_str import DBTStr
# 获取传入字符串中群员的名字，需将名字前面的字用strip割掉,返回数据库中不全的名字
class LikeMember:
    def cutMember(self, nameInContent):
        member = nameInContent[:7]
        member = member.strip(' ')
        return member

    def likeMember(self, content):
        self.content = content
        memberName = self.cutMember(self.content) + '%'
        memberName = DBHelper().selectOne(" select name from user where name like '"+memberName+"' ")
        memberName = memberName[0].__str__()
        return memberName

    #查询群员是否在数据库里
    def likeMemberBe(self,content):
        memberName = self.cutMember(content) + '%'
        if len(DBHelper().selectAll("select name from user where name like '"+memberName+"' ")) != 0:
            return True
        else:
            return False

