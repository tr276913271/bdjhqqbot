# -*- coding: UTF-8 -*-
import json, requests, random

class SingleMoliService:
    def mlservice(self, content):
        moliDate = {
            "question":content,
            "api_key":'ecb213916c9ea309282c99bae0791e8d',
            "api_secret":'6cg8y8nh7vit'
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
            return rs