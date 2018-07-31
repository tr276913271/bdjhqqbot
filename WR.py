# -*- coding:utf-8 -*-
# 色图Time
from qqbot import qqbotsched
@qqbotsched(hour='00',minute='00')
def sexTask(bot):
    gl = bot.List('group','半岛鸡盒')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, "It's 色图Time！该起床发色图啦~半姬会回避不会偷看的(>д<)")