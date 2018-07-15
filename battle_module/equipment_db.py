# -*- coding: UTF-8 -*-
from battle_module.equipment import Equipment
from db_module.connect_db import DBHelper

def initEDB():
    list = []
    db = DBHelper().selectAll("select * from equipment")
    for info in db:
        list.append(Equipment(info))
    return list

class EquipmentDB:
    EDB =initEDB()
