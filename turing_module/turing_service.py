# -*- coding: UTF-8 -*-
import json, requests, random

class TuringService:
    def service(self,content):
        d = {
          'key' : '',
          'info' : content
        }
        rs = requests.post('http://www.tuling123.com/openapi/api', data = d)
        rs = rs.text
        rs = json.loads(rs)
        if rs['code'] == 40004:
            return '本萌妹累了，明天再找我吧'
        elif rs['code'] == 100000:
            rs['text'] = rs['text'].replace('小主人','欧尼酱')
            rs['text'] = rs['text'].replace('你','欧尼酱')
            return rs['text']
        elif rs['code'] == 200000:
            rs['text'] = rs['text'].replace('亲，已帮你找到列车信息','要去千里送吗，给你')
            rs['text'] = rs['text'].replace('亲，已帮你找到图片','HSO，诺，给你')
            rs['text'] = rs['text'].replace('亲','欧尼酱')
            return rs['text'] + '\n' + rs['url']
        else:
            return '暂时不支持的技能，来个程序员啊！'
