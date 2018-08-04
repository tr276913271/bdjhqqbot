from selenium import webdriver
import time, datetime
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from qqbot import qqbotsched
from db_module.connect_db import DBHelper

@qqbotsched(hour='9,13,18,21', minute='30')
def ngaTask(bot):

    sqlMaxTime = DBHelper().selectOne("select posttime from nga where poid = 1")
    sqlMaxTime = sqlMaxTime[0].__str__()
    sqlMaxTime = datetime.datetime.strptime(sqlMaxTime,'%Y-%m-%d %H:%M:%S')
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    


    
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--user-agent=some user-agent name")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('http://nga.178.com/thread.php?fid=310')
    time.sleep(6)
    html = driver.page_source
    soap = BeautifulSoup(html)
    for rowX in soap.find_all(class_="row1 topicrow"):
        time = rowX.find(class_="silver postdate")
        time = time.get('title')
        linkspan = rowX.find(class_="topic")
        [s.extract() for s in linkspan('span')]
        link = linkspan.get('href')
        del linkspan['class']
        del linkspan['href']
        del linkspan['id']
        title = linkspan.text
        #这里有个判断
        time += ':00'
        time = '20'+time
        time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        if time > sqlMaxTime :
            DBHelper().insert("INSERT INTO `nga` (`posttime`, `superlink`, `potitle`) VALUES ('"+str(time)+"','"+str(link)+"','"+str(title)+"')")
        

    for rowX in soap.find_all(class_="row2 topicrow"):
        time = rowX.find(class_="silver postdate")
        time = time.get('title')
        linkspan = rowX.find(class_="topic")
        [s.extract() for s in linkspan('span')]
        link = linkspan.get('href')
        del linkspan['class']
        del linkspan['href']
        del linkspan['id']
        title = linkspan.text
        #这里有个判断
        time += ':00'
        time = '20'+time
        time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        if time > sqlMaxTime :
            DBHelper().insert("INSERT INTO `nga` (`posttime`, `superlink`, `potitle`) VALUES ('"+str(time)+"','"+str(link)+"','"+str(title)+"')")
        
    #更新sqlMaxTime的时间
    DBHelper().update("update nga set `posttime`='"+nowtime+"' where poid=1")