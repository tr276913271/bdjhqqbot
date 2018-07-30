from battle_module.person import Person
from battle_module.battle_dao import BattleDao

level1T = (1,1,1000,0,100,100,1,3,2,0,1000,1)
level2T = (1,1,1000,0,100,100,1,3,2,0,1000,1)
class MonsterServie(object):
    def __init__(self):
        self.level1 = Person("贪食的肥肥")
        self.level1.initWithDB(level1T)
        self.result = ""

    def hunt(self,member,type):
        dao = BattleDao()
        person = dao.selectUser(member)
        if(type==1):
            self.result = "你找到了贪食肥肥Neet之处!肥肥正在吃鸡盒！讨伐开始\n"
            result,flag,process = person.battleWith(self.level1)
            self.result += result
            self.level1.hp = self.level1.maxhp
            dao.updateBattleInfo(person)
        return self.result
