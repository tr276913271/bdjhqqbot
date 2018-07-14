import random

class Roll:
    def shouldService(self, content):
        if (content.startswith('roll')):
            return True
        else :
            return False

    def roll(self, content):
        if (not content.startswith("roll")):
            return 0
        try:
            strlist = content.split(" ")
            result = 0
            if (len(strlist) > 1):
                result = random.randint(0, int(strlist[1]))
            else :
                result = random.randint(0, 100)
        except:
            result = random.randint(0, 100)
        return str(result)
