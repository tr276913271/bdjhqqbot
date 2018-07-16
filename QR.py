#- * -coding: utf - 8 - * -
from other_module.sensitive_words import SensitiveWorldModule
from bulletin_board_module.bulletin_board import BBS
from other_module.roll import Roll
from wow_module.wowplay import WowPlayService
from other_module.imoutotime import TimeService
from big_gay_module.sign_in import SignInSystem
from turing_module.turing_service import TuringService
from wow_module.looking_for_group import LookingForGroupService
from other_module.parents import ParentService
from remote_module.supervise import AdminSupervise
#from mock_bot import MockBot


def onQQMessage(bot, contact, member, content):
    if content[: 5: ] != '[@ME]':
        return 0
    content = content[7:]
    ## 如果是敏感词
    if (SensitiveWorldModule().isSensitiveWorld(content)):
        return 0
    ## 公告功能
    elif (BBS().shouldService(content)):
        bot.SendTo(contact, BBS().service(content))
    ## WOW打本吆喝
    elif (LookingForGroupService().shouldService(member.name,content)):
        bot.SendTo(contact, LookingForGroupService().service(member.name))
    # 妹妹时间
    elif content == '':
        bot.SendTo(contact, TimeService().iotimes() + member.name)
    # 妈妈爸爸
    elif (ParentService().parent(content)):
      bot.SendTo(ParentService().parent(content))
    
    #elif content == '你该睡觉了QWER':
        #if member.name == '想要过平静生活的七花' or member.name == '所有人都过来/zs/酒仙':
            #bot.SendTo(contact, '好的，我去睡觉了~')
            #bot.Stop()
    # ROLL点
    elif (Roll().shouldService(content)):
        bot.SendTo(contact, Roll().roll(content))
    # WOW玩什么职业
    elif (WowPlayService().shouldService(content)):
        bot.SendTo(contact, WowPlayService().service())
    # 大给币签到系统
    elif (SignInSystem().shouldService(content)):
        bot.SendTo(contact, SignInSystem().service(member.name,content))
    # 远程关闭
    elif (AdminSupervise().turnOff(content, member.name))
        return 0
    # 图灵API
    else :
        bot.SendTo(contact, TuringService().service(content))

# if __name__ == '__main__':
#     onQQMessage(MockBot(), "aa", "bb", "[@ME]..求组队")
#     onQQMessage(MockBot(), "aa", "asabb", "[@ME]..求组队")
#     print(LookingForGroupService.ticks)
