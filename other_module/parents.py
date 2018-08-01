# -*- coding: utf-8 -*-

class ParentService:


  def parent(self, content):
  
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
    elif (content.find('小姨') >= 0):
        contents = '是零七小阿姨哦~她超可爱的~'
    else:
        contents = False
    return contents

