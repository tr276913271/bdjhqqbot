# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
class himeBus:
    def driverHimeif(self,content):
        if content.find('车牌：') >= 0:
            return True
        else:
            return False

    def driverHime(self,content):
        content = content.strip('车牌：')
        content = content.strip(' ')
        px = {'http': 'http://127.0.0.1:1081','https':'https://127.0.0.1:1081'}
        try:
            r = requests.get("https://btso.pw/search/" + content, proxies=px)
            r.raise_for_status()
            soup = BeautifulSoup(r.text)
            dataAll = soup.select('div[class="row"]')
            sizeIntZ = 100
            for  rowX in dataAll:
                dataS = rowX.find(class_="col-sm-2 col-lg-1 hidden-xs text-right size")
                if dataS is not None:
                    cutSize = dataS.text[:-2]
                    sizeInt = float(cutSize)
                    if sizeInt < sizeIntZ:
                        sizeIntZ = sizeInt
                        data = rowX.find('a')
                        linkTemp = data.get('href')
            
            rMagnet = requests.get(linkTemp, proxies=px)
            r.raise_for_status()
            soupMagnet = BeautifulSoup(rMagnet.text)
            magnetLink = soupMagnet.find('textarea')
            return magnetLink.text
        except:
            print ('error')
