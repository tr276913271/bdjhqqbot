import random

from battle_module import *


if __name__ == '__main__':
    for e in equipment_db.EquipmentDB.EDB:
        print(e.showInfo())


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
