# -*- coding: utf-8 -*-

def parent(content):
  if (content.find('爸妈') >= 0):
    contents = '我爸爸妈妈是七花和妹控哦~'
  elif (content.find('爸爸妈妈') >= 0):
    contents = '我爸爸妈妈是七花和妹控哦~'
  elif (content.find('爸爸和妈妈') >= 0):
    contents = '我爸爸妈妈是七花和妹控哦~'
  elif (content.find('爸爸') >= 0):
    contents = '我爸爸是七花哦~'
  elif (content.find('妈妈') >= 0):
    contents = '我妈妈是白丝JK妹控哦~'
  elif (content.find('父母') >= 0):
    contents = '我爸爸妈妈是七花和妹控哦~'
  elif (content.find('爹') >= 0):
    contents = '我爸爸是七花哦~'
  else:
    contents = False
  return contents

     
