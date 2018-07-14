#- * -coding: utf - 8 - * -
import time, json, random
int_file = 'C:\\Users\\Edward\\.qqbot-tmp\\plugins\\jj.json'
class SignInService:


    def shouldService(self,content):
        print(content)
        if content == '大给币':
            return True
        if content == '查询':
            return True
        return False

    def service(self,member,content):
        if content == '大给币':
            return self.signIn(member)
        if content == '查询':
            return self.queryIn(member)

    def signIn(self,member):
        with open(int_file, 'r') as file_gai:
            gourpMembers = json.load(file_gai)

        time_today = str(time.localtime(time.time()).tm_mon) + str(time.localtime(time.time()).tm_mday)
        gourpMembers['today'] = time_today

        if gourpMembers.__contains__(member) == False:
            gourpMembers[member] = ['0', 0]

        memberStatus = gourpMembers[member]
        todaytime = gourpMembers['today']

        if memberStatus[0] != todaytime:
            memberStatus[0] = todaytime
            todayIncrement = random.randint(1, 10)
            memberStatus[1] += todayIncrement
            menstr = '耶~' + member + '欧尼酱今天获取了' + str(todayIncrement) + '个大给币！' + '\n欧尼酱现在一共有' + str(memberStatus[1]) + '个大给币哟~'
            gourpMembers[member] = memberStatus
            with open(int_file, 'w') as file_gai:
                json.dump(gourpMembers, file_gai)
        else :
            menstr = '欧尼酱今天已经领取过大给币了~再乱来小心扣你大给币！( `д´)'
        return menstr

    def queryIn(self,member):
        with open(int_file, 'r') as file_gai:
            gourpMembers = json.load(file_gai)
            memberStatus = gourpMembers[member]
        if gourpMembers.__contains__(member) == False:
            Increment = '欧尼酱你还没有大给币哦，先签到领取一个吧~'
        else :
            Increment = '欧尼酱有' + str(memberStatus[1]) + '个大给币呢~~'
        return Increment
