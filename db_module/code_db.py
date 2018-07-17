# -*- coding: utf-8 -*-
from db_module.connect_db import DBHelper
import json

class CodeBean:
    def __init__(self,tuple):
        self.code = tuple[1]
        self.codeName = tuple[2]
        self.codeType = tuple[3]
    def __str__(self):
        return json.dumps(self,default=lambda obj: obj.__dict__,ensure_ascii=False)
    def __repr__(self):
        return json.dumps(self,default=lambda obj: obj.__dict__,ensure_ascii=False)

def initCodeDB():
    dict = {}
    db = DBHelper().selectAll("select * from code")
    for info in db:
        if(not dict.__contains__(info[3])):
            dict[info[3]] = []
        dict[info[3]].append(CodeBean(info))
    return dict

class CodeDBService:
    CodeDB =initCodeDB()
