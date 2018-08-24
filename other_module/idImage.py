# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

class idImageSuperLink:
    def identifyFun(self,content):
        try:
            r = requests.get("https://image.baidu.com/n/pc_search?queryImageUrl=" + content + "&uptype=urlsearch" , timeout = 6)
            r.raise_for_status()

            soup = BeautifulSoup(r.text)
            dataName = soup.find(class_="guess-newbaike-profession")
            if dataName != None:
                menstr = "你要找的是不是" + dataName.text + "?"
            else:
                htmlstr = r.text
                startNum = htmlstr.find('guessWord')
                htmlstr = htmlstr[startNum:]
                endNum = htmlstr.find('.split')
                htmlstr = htmlstr[13:endNum-1]
                if len(htmlstr) == 0:
                    menstr = "半姬不知道你搜的是什么哦"
                else:
                    menstr = "你要找的是不是" + htmlstr + "?"
        except:
            print("error2")
            menstr = "报错了"
        return menstr

    def identifyIf(self,content):
        if content.find('识图：') >=0:
            return True
        else:
            return False

    def identifyImage(self,content):
        content = content.strip('识图：')
        content = content.strip(' ')
        try:
            r = requests.get(content)
            if r.status_code != 200:
                menstr = "需要图片的链接哦"
            else:
                menstr = self.identifyFun(content)
        except:
            print("error")
            menstr = "报错了"
        return menstr