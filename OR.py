# -*- coding: utf-8 -*-
import json, requests, random
import wowplay, imoutotime, parents, qiandao
from  sensitive_words import SensitiveWorldModule

def onQQMessage(bot, contact, member, content):
  if content[:5:] != '[@ME]':
     return 0
  content = content[7:]
  ##如果是敏感词
  if(SensitiveWorldModule().isSensitiveWorld(content)):
	  return 0

  if content == '':
    bot.SendTo(contact,imoutotime.iotimes() + member.name)
  elif (parents.parent(content)):
    bot.SendTo(contact,parents.parent(content))
  elif content == '你该睡觉了':
    bot.SendTo(contact,'本萌妹睡了，不要喊我了')
    bot.Stop()
  elif content == '大给币':
    bot.SendTo(contact,qiandao.signIn(member.name))
  elif content == '查询':
    bot.SendTo(contact,qiandao.queryIn(member.name))
  elif content.startswith('roll'):
    bot.SendTo(contact,roll(content))
#  elif wowplay.shouldService(contact):
#    bot.SendTo(contact,'获得返回值')
  elif (content.find('8.0玩什么') >= 0):
    bot.SendTo(contact,wowplay.wowplaysr())
  elif (content.find('下版本玩什么') >= 0):
    bot.SendTo(contact,wowplay.wowplaysr())
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
      rs['text'] = rs['text'].replace('小主人','欧尼酱')
      rs['text'] = rs['text'].replace('你','欧尼酱')
      bot.SendTo(contact,rs['text'])
    elif rs['code'] == 200000:
      rs['text'] = rs['text'].replace('亲，已帮你找到列车信息','要去千里送吗，给你')
      rs['text'] = rs['text'].replace('亲，已帮你找到图片','HSO，诺，给你')
      rs['text'] = rs['text'].replace('亲','欧尼酱')
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
      result = str(result)
    else:
      result = random.randint(0,100)
      result = str(result)
  except:
    result = random.randint(0,100)
    result = str(result)
  return result

#######################################
#这里的内容以后移到别的地方去
#本萌妹受不了了
#放到别的文件里就调用不了，狗屎
#
#
#######################################

