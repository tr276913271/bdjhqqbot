#- * -coding: utf - 8 - * -
from other_module.sensitive_words import SensitiveWorldModule
from bulletin_board_module.bulletin_board import BBS
from other_module.roll import Roll
from wow_module.wowplay import WowPlayService
from other_module.imoutotime import TimeService
from big_gay_module.sign_in import SignInService
from turing_module.turing_service import TuringService
from wow_module.looking_for_group import LookingForGroupService
from other_module.parents import ParentService
from battle_module import BattleService
#from mock_bot import MockBot


def onQQMessage(bot, contact, member, content):
    if content[: 5: ] != '[@ME]':
        return 0
    content = content[7:]
    ## 如果是敏感词
    if (SensitiveWorldModule().isSensitiveWorld(content)):
        return 0
    ## 如果是敏感词
    if (BattleService().shouldService(content)):
        return bot.SendTo(contact, BattleService().service(content))
    ## 公告功能
    if (BBS().shouldService(content)):
        return bot.SendTo(contact, BBS().service(content))
    ## WOW打本吆喝
    if (LookingForGroupService().shouldService(member.name,content)):
        return bot.SendTo(contact, LookingForGroupService().service(member.name))
    # 妹妹时间
    if content == '':
        return bot.SendTo(contact, TimeService().iotimes() + member.name)
    # 妈妈爸爸
    elif (ParentService().parent(content)):
        return bot.SendTo(ParentService().parent(content))
    # 远程关闭
    elif content == '你该睡觉了QWER':
        if member.name == '想要过平静生活的七花' or member.name == '所有人都过来/zs/酒仙':
            bot.SendTo(contact, '好的，我去睡觉了~')
            bot.Stop()
            return
    # ROLL点
    elif (Roll().shouldService(content)):
        return bot.SendTo(contact, Roll().roll(content))
    # WOW玩什么职业
    elif (WowPlayService().shouldService(content)):
        return bot.SendTo(contact, WowPlayService().service())
    # 大给币签到系统
    elif (SignInService().shouldService(content)):
        return bot.SendTo(contact, SignInService().service(member.name,content))
    # 图灵API
    else :
        return bot.SendTo(contact, TuringService().service(content))

# if __name__ == '__main__':
#     onQQMessage(MockBot(), "aa", "bb", "[@ME]..人物信息")
