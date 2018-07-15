# -*- coding: UTF-8 -*-
from battle_module.equipment import Equipment
from db_module.connect_db import DBHelper

def initEDB():
    dict = {}
    db = DBHelper().selectAll("select * from equipment")
    for info in db:
        dict[info[0]]=Equipment(info)
    return dict

class EquipmentDB:
    EDB =initEDB()

    def initPerson(p):
        p.weapon = EquipmentDB.EDB[2]
        p.head = EquipmentDB.EDB[1]
        p.breast = EquipmentDB.EDB[3]
