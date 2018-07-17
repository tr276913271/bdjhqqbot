import random
import math
from battle_module import *
from db_module.connect_db import *
from db_module.code_db import *

if __name__ == '__main__':
    # print(CodeDBService.CodeDB['职业类型'])
    # print(battle_service.BattleService().service("sssssss"))
    p = battle_service.BattleService().getPerson("sssssss")
    p1 = battle_service.BattleService().getPerson("sssss11ss")
    print(p.battleWith(p1))
    print(p.showInfo())
    # print(p.showInfo())
    # print(p.battleWith(11))
    # print(DBHelper().selectOne("select * from user where id=1"))
    # for e in equipment_db.EquipmentDB.EDB:
    #     print(equipment_db.EquipmentDB.EDB[e].showInfo())


'''
本馆101孬102球103介104被炸毁105所有人106小马107七花108真红
201羞202豆203（闹鬼门被钉死）204-206空207 07 JJ 208奶爸
别馆101少爷  201老爷
图书馆没人
体育仓库没人
本馆地下室有衰三
'''

'''
|-------------------------------------|
|             |       |               |
|             |       |               |
|    101      |       |     105       |
|             |       |               |
|             |       |               |
|             |       |               |
|             |       |               |
|-------------|       |---------------|
|             |       |               |
|             |       |               |
|             |       |     106       |
|    102      |       |               |
|             |       |               |
|             |       |---------------|---
|             |
|-------------|
|             |
|             |       |---------------|---
|             |       |               |
|    103      |       |               |
|             |       |      107      |
|             |       |               |
|             |       |               |
|-------------|       |---------------|
|             |       |               |
|             |       |               |
|             |       |               |
|    104      |       |      108      |
|             |       |               |
|             |       |               |
|             |       |               |
|             |       |               |
|-------------------------------------|
'''

def urineHomeInfo(content):
  return 0
