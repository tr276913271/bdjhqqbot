# -*- coding:utf-8 -*-
# 色图Time
from qqbot import qqbotsched
import time
@qqbotsched(hour='00',minute='00')
def sexTask(bot):
    gl = bot.List('group','半岛鸡盒')
    gt = time.strftime("%Y-%m-%d", time.localtime())
    if gl is not None:
        for group in gl:
            bot.SendTo(group, "现在是"+ gt + "00：00 ~" +"It's 色图Time！该起床发色图啦~半姬会回避不会偷看的(>д<)")