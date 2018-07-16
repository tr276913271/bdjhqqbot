#- * -coding: utf - 8 - * -

class AdminSupervise:
    def administrator (self, member):
        if member == '想要过平静生活':
            return True
        elif member =='所有人都过来/zs':
            return True
        elif member =='afk的咸鱼':
            return True
        else:
            return False

    def turnOff(self,content,member):
        if self.administrator(member):
            if content == '半姬睡觉吧':
                bot.Stop()
                return 0
        else :
            return False
