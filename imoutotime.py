# -*- coding: utf-8 -*-
import  time, requests

def iotimes():
  iotime = (time.strftime("%H", time.localtime()))
  iotime = int(iotime)

  iotimenow = time.strftime("%Y-%m-%d %H:%M", time.localtime())
  

  if iotime < 6:
    iotimefun = '这都几点了，欧尼酱修仙嘛(　д ) ﾟ ﾟ'
  elif iotime < 8:
    iotimefun = '欧尼酱该起床上班赚钱养活我了(=ﾟωﾟ)='
  elif iotime < 11:
    iotimefun = '大上午的就在摸鱼，哼(￣︿￣)'
  elif iotime < 13:
    iotimefun = '午休时间咯，欧尼酱睡个午觉啦(￣3￣)'
  elif iotime < 18:
    iotimefun = '下午是摸鱼的好时间哦，摸一会就能下班了(*´ω`*)'
  elif iotime < 23:
    iotimefun = '现在是游戏时间！有没有好哥哥一起来玩游戏呀(´・ω・`)'
  elif iotime >= 23:
    iotimefun = '好孩子们该睡觉觉啦！ヾ(´ωﾟ｀)'
  iotimefun = '当前时间是' + iotimenow + '哟！~' + '\n' + iotimefun
  return iotimefun