# -*- coding: UTF-8 -*-
import json, requests, random

class MoliService:
    def mlservice(self, content):
        moliDate = {
            "question":content,
            "api_key":'',
            "api_secret":''
        }
        rs = requests.post('http://i.itpk.cn/api.php', data = moliDate)
        rs = rs.text
        return rs