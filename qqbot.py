# -*- coding: utf-8 -*-
import json, requests, random
def onQQMessage(bot, contact, member, content):
  if content[:5:] != '[@ME]':
     return 0
  content = content[7:]

  if content == '':
    bot.SendTo(contact,'嗨哆磨，在下SuperAI！')
  elif content == '你该睡觉了':
    bot.SendTo(contact,'本萌妹睡了，不要喊我了')
    bot.Stop()
  elif content.startswith('roll'):
    bot.SendTo(contact,roll(content))
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

def roll(content):
  if(not content.startswith("roll")):
    return 0
  try:
    strlist = content.split(" ")
    result = 0
    if(len(strlist)>1):
      result = random.randint(0,int(strlist[1]))
    else:
      result = random.randint(0,100)
  except:
    result = random.randint(0,100)
  return result