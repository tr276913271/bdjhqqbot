# -*- coding: utf-8 -*-
import json, requests
def onQQMessage(bot, contact, member, content):
  if content[:5:] != '[@ME]':
     return 0
  content = content[7:]

  if content == '':
    bot.SendTo(contact,'嗨哆磨，在下SuperAI！')
  elif content == '你该睡觉了':
    bot.SendTo(contact,'本萌妹睡了，不要喊我了')
    bot.Stop()
  else:
    d = {
      'key' : '',
      'info' : content
    }
    rs = requests.post('http://www.tuling123.com/openapi/api', data = d)
    rs = rs.text
    rs = json.loads(rs)
    if rs['code'] == 40004:
      bot.SendTo(contact,'本萌妹累了，明天再找我吧')
    elif rs['code'] == 100000:
      bot.SendTo(contact,rs['text'])
    elif rs['code'] == 200000:
      bot.SendTo(contact,rs['text'] + '\n' + rs['url'])
    else:
      bot.SendTo(contact,'暂时不支持的技能，来个程序员啊！')
