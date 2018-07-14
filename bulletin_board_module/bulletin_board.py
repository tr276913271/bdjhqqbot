# -*- coding: UTF-8 -*-

class BBS:
    def shouldService(self,content):
        list = content.split(" ")
        if(list[0]=="半姬私语"):
            return True
        elif(list[0]=="半姬私语设置"):
            return True
        else:
            return False

    def setBoardInfo(self,content):
        self.board = content

    def service(self,content):
        list = content.split(" ")
        if(list[0]=="半姬私语"):
            return self.board
        elif(list[0]=="半姬私语设置"):
            self.setBoardInfo(list[1])
            return "设置成功"
        return "啦啦啦"

    def __init__(self):
        self.board = ""


if __name__ == '__main__':
    b = BBS()
    if(b.shouldService("半姬私语设置")):
        print(b.service("半姬私语设置 隧道发生的"))
        print(b.service("半姬私语"))
