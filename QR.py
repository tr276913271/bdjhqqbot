#- * -coding: utf - 8 - * -
from other_module.sensitive_words import SensitiveWorldModule
from bulletin_board_module.bulletin_board import BBS
from other_module.roll import Roll
from wow_module.wowplay import WowPlayService
from other_module.imoutotime import TimeService
from big_gay_module.sign_in import SignInService
from turing_module.turing_service import TuringService
from wow_module.looking_for_group import LookingForGroupService
#from mock_bot import MockBot


def onQQMessage(bot, contact, member, content):
    if content[: 5: ] != '[@ME]':
        return 0
    content = content[7:]## 如果是敏感词

    if (SensitiveWorldModule().isSensitiveWorld(content)):
        return 0## 公告功能
    if (BBS().shouldService(content)):
        return BBS().service(content)
    if (LookingForGroupService().shouldService(member,content)):
        return bot.SendTo(contact, LookingForGroupService().service(member))
    if content == '':
        bot.SendTo(contact, TimeService().iotimes() + member.name)
    elif content == '你该睡觉了QWER':
        bot.SendTo(contact, '本萌妹睡了，不要喊我了')
        bot.Stop()
    elif Roll().shouldService(content):
        bot.SendTo(contact, Roll().roll(content))
    elif WowPlayService().shouldService(content):
        bot.SendTo(contact, WowPlayService().service())
    elif SignInService().shouldService(content):
        bot.SendTo(contact, SignInService().service(member.name,content))
    else :
        bot.SendTo(contact, TuringService().service(content))

# if __name__ == '__main__':
#     onQQMessage(MockBot(), "aa", "bb", "[@ME]..求组队")
#     onQQMessage(MockBot(), "aa", "asabb", "[@ME]..求组队")
#     print(LookingForGroupService.ticks)
