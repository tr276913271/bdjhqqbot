# -*- coding: UTF-8 -*-
import json, requests, random

class SingleMoliService:
    def mlservice(self, content,qqName):
        moliDate = {
            "question":content,
            "api_key":'',
            "api_secret":''
        }
        rs = requests.post('http://i.itpk.cn/api.php', data = moliDate)
        rs = rs.text
        if content == '月老灵签':
            if rs.startswith(u'\ufeff'):
                rs = rs.encode('utf8')[3:].decode('utf8')
                rs = json.loads(rs, encoding='utf8')
                rs = rs['number2'] + " 卦象：" + rs['haohua'] + " 诗意：" + rs['shiyi'] + " 解签：" + rs['jieqian']
            return rs
        elif content == '笑话' or content == '灵签':
            rs = '暂时不支持的功能哦~'
            return rs
        else:
            if qqNumber == '315451609':
                rs = rs.replace('你','爸爸')
            return rs