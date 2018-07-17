#- * -coding: utf - 8 - * -
import time
from db_module.connect_db import DBHelper
#member = '铁花'
#timeToday = time.strftime("%Y-%m-%d", time.localtime())
#memberId = DBHelper().selectOne("select id from user where name = '"+member+"' ")
#memberId = memberId[0].__str__()
#theftNumber = DBHelper().selectOne("select count(*) from theft where theftUserid = '"+memberId+"' and theftDate = '"+timeToday+"'")
#theftNumber = theftNumber[0].__str__()

#print (theftNumber)
memberName = 'test123'
a = len(DBHelper().selectOne("select name from user where name like '"+memberName+"' ")) 
print(a)