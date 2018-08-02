# -*- coding: UTF-8 -*-
def strToInt(content):
    try:
        eid = int(content)
        return True,eid
    except Exception as e:
        return False,0
