from battle_module.person import Person

level1T = (1,1,1000,0,100,100,1,3,2,0,1000,1)
level2T = (1,1,1000,0,100,100,1,3,2,0,1000,1)
class MonsterServie(object):
    def __init__(self):
        self.level1 = Person("贪食的肥肥")
        self.level1.initWithDB(level1T)
