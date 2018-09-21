# -*- coding:utf-8 -*-
# 自动天气
from qqbot import qqbotsched
from singlepoeple_moudule.singlemoli import SingleMoliService

@qqbotsched(hour='09',minute='30')
def weatherTime(bot):
    menstr = SingleMoliService().mlservice('常州天气','填充字符')
    bl = bot.List('buddy','铁花')
    if bl:
        b = bl[0]
        bot.SendTo(b,menstr)