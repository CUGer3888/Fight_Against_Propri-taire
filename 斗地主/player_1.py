import requests  # 发送请求
import re


def get_data():
    url = "https://api.bilibili.com/x/v2/reply/wbi/main?oid=1011139183900622865&type=17&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=4d3c974e3bb39681d86e8ce68426e53b&wts=1734344480"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }
    response = requests.get(url, headers=header)
    datas = response.json()['data']['replies']
    lis = []
    for data in datas:
        lis.append(data["content"]["message"])
    return lis


"""
{'if_start': 0, 
'player_1': 【3, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 10, 10, 11, 12, 13, 14, 17】, 
'player_2': 【3, 4, 5, 6, 6, 7, 7, 8, 8, 9, 10, 11, 11, 12, 14, 14, 15, 15】,
'player_3': 【3, 3, 4, 4, 9, 9, 9, 10, 11, 12, 12, 13, 13, 13, 14, 15, 15, 16】, 'current_player': 0}
"""

def translate(step):
    #对A，2，J,Q,K进行翻译
    if 'A' in step:
        pass



def comment(str):
    url = "https://api.bilibili.com/x/v2/reply/add"
    data = {
        "plat": 1,
        "oid": "1011139183900622865",
        "type": "17",
        "message": str,
        "gaia_source": "main_web",
        "csrf": "af0210fda7da18a136f29acb4fbf1414",
        "ordering":"heat",
        "jsonp":"jsonp",
    }
    header={
        "cookie":"buvid3=63F2A07D-B1B2-5827-69B6-A85425C0BFC447917infoc; b_nut=1712821447; _uuid=BE5A3EC6-C910A-19AC-B5E7-73F6A9F10894A48359infoc; buvid4=1E201E00-65BC-BB72-D7C5-33C0DDE6CD3348900-024041107-VEkFsVIYhyuHFNlQUcADvw%3D%3D; rpdid=|(mmRl~uRu)0J'u~uk)kuRRm; DedeUserID=693537580; DedeUserID__ckMd5=c6c6c4798be9b9b3; buvid_fp_plain=undefined; enable_web_push=DISABLE; FEED_LIVE_VERSION=V_DYN_LIVING_UP; header_theme_version=CLOSE; is-2022-channel=1; hit-dyn-v2=1; LIVE_BUVID=AUTO4217132695647997; PVID=2; dy_spec_agreed=1; blackside_state=0; CURRENT_BLACKGAP=0; CURRENT_QUALITY=127; fingerprint=36cc6340c61e4376f0def49a1b42e8c2; home_feed_column=5; browser_resolution=1920-925; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQ0MjI1MTIsImlhdCI6MTczNDE2MzI1MiwicGx0IjotMX0.q1MCb-OkbNg8xR4J4qWftMKamnWxDcE1P-BF-2EJvcY; bili_ticket_expires=1734422452; SESSDATA=e2367de6%2C1749722023%2Ced929%2Ac2CjB6kCQJf82TkJQu889xqN-c0iK5BFeyuyPApHddrw0utezae3_1dEshC-WWFphetvgSVmoyM0JmeFdZMmpoY3JDeVBBX2xXZTBRX3RZQlcyemJ1WWI4U3EwSUNQVDgySnlWVGJjTG90VkI5TTJocTMwLWdjRWtkQ0tzQnFPNkkzRDJGNDVMUHlRIIEC; bili_jct=af0210fda7da18a136f29acb4fbf1414; bp_t_offset_693537580=1010989409752842240; b_lsid=4FA104892_193CA1B6EF0; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; bsource=search_bing; buvid_fp=36cc6340c61e4376f0def49a1b42e8c2; sid=6ncetye6; CURRENT_FNVAL=4048",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }
    response = requests.post(url=url, data=data,headers=header)
    if response.status_code == 200:
        print("评论成功")
    else:
        print("评论失败")



def find_card():
    now_data = get_data()
    # print(now_data[0])
    # print(type(now_data[0]))
    sting = now_data[0]
    sting = sting.replace('【','[')
    sting = sting.replace('】',']')
    data_dir = eval(sting)
    # print(data_dir)
    #找到player_1的牌  'player_1': 到】,
    player_1 = re.findall(r'player_1(.+?)】,', now_data[0])
    # print(player_1[0][4:-4])
    now_card = []
    for i in player_1[0][4:].split(','):
        now_card.append(int(i.strip()))
    return now_card,data_dir


# now_data = get_data()
# current_player = re.findall(r"current_player(.+?)current_cards",now_data[0])
# current_player = int(current_player[0][3])
#得到当前是谁在出牌
#解析出牌

def parse_card(card,step):
    if "过" in step:
        # print(0)
        lis = step.split(" ")
        chupai = int(lis[1])
        if chupai in card:
            print("有,出牌成功")
            card.remove(chupai)
            tmp_card = "["+str(chupai)+"]"
            # print(card,tmp_card)
        else:
            print("没有，出牌失败")
    if "对" == step[0]:
        # print(1)
        lis = step.split(" ")
        chupai = int(lis[1])
        print(chupai)
        if chupai in card and card.count(chupai) >= 2:
            print("有,出牌成功")
            card.remove(chupai)
            card.remove(chupai)
            tmp_card = "["+str(chupai)+","+str(chupai)+"]"
            # print(card,tmp_card)
        else:
            print("没有，出牌失败")

    if "三带一" in step:
        # print(2)
        lis = step.split(" ")
        card_1 = int(lis[1])
        card_2 = int(lis[3])
        if card_1 in card and card_2 in card and card.count(card_1) >= 3:
            print("有,出牌成功")
            for i in range(3):
                card.remove(card_1)
            card.remove(card_2)
            tmp_card = "["+str(card_1)+","+str(card_1)+","+str(card_1)+","+str(card_2)+"]"
            # print(card,tmp_card)
        else:
            print("没有，出牌失败")
    if "三带二" in step:
        # print(3)
        lis = step.split(" ")
        card_1 = int(lis[1])
        card_2 = int(lis[3])
        if card_1 in card and card_2 in card and card.count(card_1) >= 3 and card.count(card_2) >= 2:
            print("有,出牌成功")
            for i in range(3):
                card.remove(card_1)
            for i in range(2):
                card.remove(card_2)
            tmp_card = "["+str(card_1)+","+str(card_1)+","+str(card_1)+","+str(card_2)+","+str(card_2)+"]"
            # print(card,tmp_card)
        else:
            print("没有，出牌失败")
    if "顺子" in step:
        # print(4)
        lis = step.split(" ")
        card_1 = int(lis[1])
        card_2 = int(lis[3])
        a=0
        for i in range(card_1,card_2+1):
            if i in card:
                pass
            else:
                a=1
        if a==0:
            print("有,出牌成功")
            tmp_card = '['
            for i in range(card_1,card_2+1):
                card.remove(i)
                tmp_card = tmp_card + str(i) + ","
            tmp_card = tmp_card[:-1] + "]"
            # print(card,tmp_card)
        else:
            print("没有，出牌失败")
    if "连对" in step:
        # print(5)
        lis = step.split(" ")
        card_1 = int(lis[1])
        card_2 = int(lis[3])
        a=0
        for i in range(card_1,card_2+1):
            if card.count(i) >= 2:
                pass
            else:
                a=1
        if a==0:
            print("有,出牌成功")
            tmp_card = "["
            for i in range(card_1,card_2+1):
                card.remove(i)
                card.remove(i)
                tmp_card = tmp_card + str(i) + "," + str(i) + ","
            tmp_card = tmp_card[:-1] + "]"
            # print(card,tmp_card)
        else:
            print("没有，出牌失败")
    if "飞机" in step:
        # print(6)
        lis = step.split(" ")
        card_1 = int(lis[1])
        card_2 = int(lis[2])
        card_3 = int(lis[4])
        card_4 = int(lis[5])
        if card.count(card_1) >= 3 and card.count(card_2) >= 3 and card.count(card_3) >= 1 and card.count(card_4) >= 1:
            print("有,出牌成功")
            tmp_card = '['
            for i in range(3):
                card.remove(card_1)
                card.remove(card_2)
                tmp_card = tmp_card + str(card_1) + "," + str(card_2) + ","
            card.remove(card_3)
            card.remove(card_4)
            tmp_card = tmp_card + str(card_3) + "," + str(card_4) + "]"
            # print(card,tmp_card)
        else:
            print("没有，出牌失败")
    if "炸弹" in step:
        # print(7)
        lis = step.split(" ")
        card_1 = int(lis[1])
        if card.count(card_1) >= 4:
            print("有,出牌成功")
            tmp_card = '['
            for i in range(4):
                card.remove(card_1)
                tmp_card = tmp_card + str(card_1) + ","
            tmp_card = tmp_card[:-1] + "]"
            # print(card,tmp_card)
        else:
            print("没有，出牌失败")
    if "王炸" in step:
        # print(8)
        if 14 in card and 15 in card:
            print("有,出牌成功")
            card.remove(14)
            card.remove(15)
            tmp_card = '[14,15]'
            # print(card,tmp_card)
        else:
            print("没有，出牌失败")
    return card,tmp_card

def get_last_step(dirs):
    last = dirs["current_cards"]
    if len(last)==0:
        #是你的回合
        return 0
    if len(last)==1:
        #过
        return "过"+" "+ str(last[0])
    elif len(last)==2:
        if last[0] == last[1]:
            #对子
            return "对"+" "+ str(last[0])
        else:
            #王炸
            return "王炸"
    elif len(last)==4:
        if last[0] == last[1] and last[1] == last[2] and last[2] == last[3]:
            #炸弹
            return "炸弹"+" "+ str(last[0])
        else:
            #三带一
            return "三带一"+" "+ str(last[0])+" "+ str(last[3])
    elif len(last) == 5:
        if last[0] == last[1]:
            # 三带二
            return "三带二"+" "+ str(last[0])+" "+ str(last[4])
        if int(last[0])+1 == int(last[1]):
            #顺子
            return "顺子"+" "+ str(last[0])+" "+"~"+" "+ str(last[-1])
    elif len(last)==8:
        if last[0] == last[1] and last[1] == last[2] :
            #飞机
            return "飞机"+" "+ str(last[0])+" "+ str(last[3])+" "+"~"+" "+ str(last[6])
    else:
        if last[0]==last[1]:
            #连对
            return "连对"+" "+ str(last[0])+" "+"~"+" "+ str(last[-1])
        else:
            #顺子
            return "顺子"+" "+ str(last[0])+" "+"~"+" "+ str(last[-1])

def clear():
    def get_rp_id():
        url = "https://api.bilibili.com/x/v2/reply/wbi/main?oid=1011139183900622865&type=17&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=1044f149e9f46fa3bbb64d0fc3a6531f&wts=1734268044"
        header = {
            "cookie": "buvid3=63F2A07D-B1B2-5827-69B6-A85425C0BFC447917infoc; b_nut=1712821447; _uuid=BE5A3EC6-C910A-19AC-B5E7-73F6A9F10894A48359infoc; buvid4=1E201E00-65BC-BB72-D7C5-33C0DDE6CD3348900-024041107-VEkFsVIYhyuHFNlQUcADvw%3D%3D; rpdid=|(mmRl~uRu)0J'u~uk)kuRRm; DedeUserID=693537580; DedeUserID__ckMd5=c6c6c4798be9b9b3; buvid_fp_plain=undefined; enable_web_push=DISABLE; FEED_LIVE_VERSION=V_DYN_LIVING_UP; header_theme_version=CLOSE; is-2022-channel=1; hit-dyn-v2=1; LIVE_BUVID=AUTO4217132695647997; PVID=2; dy_spec_agreed=1; blackside_state=0; CURRENT_BLACKGAP=0; CURRENT_QUALITY=127; fingerprint=36cc6340c61e4376f0def49a1b42e8c2; home_feed_column=5; browser_resolution=1920-925; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQ0MjI1MTIsImlhdCI6MTczNDE2MzI1MiwicGx0IjotMX0.q1MCb-OkbNg8xR4J4qWftMKamnWxDcE1P-BF-2EJvcY; bili_ticket_expires=1734422452; SESSDATA=e2367de6%2C1749722023%2Ced929%2Ac2CjB6kCQJf82TkJQu889xqN-c0iK5BFeyuyPApHddrw0utezae3_1dEshC-WWFphetvgSVmoyM0JmeFdZMmpoY3JDeVBBX2xXZTBRX3RZQlcyemJ1WWI4U3EwSUNQVDgySnlWVGJjTG90VkI5TTJocTMwLWdjRWtkQ0tzQnFPNkkzRDJGNDVMUHlRIIEC; bili_jct=af0210fda7da18a136f29acb4fbf1414; b_lsid=4FA104892_193CA1B6EF0; bsource=search_bing; sid=6ncetye6; bp_t_offset_693537580=1011152300682510336; CURRENT_FNVAL=4048; buvid_fp=36cc6340c61e4376f0def49a1b42e8c2",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
        }
        response = requests.get(url=url, headers=header)
        rpid = re.findall(r'"rpid":(\d+)', response.text)
        return rpid
    def del_comment(rpid):
        data = {
            "oid": "1011139183900622865",
            "type": "17",
            "rpid": rpid,
            "csrf": "af0210fda7da18a136f29acb4fbf1414",
        }
        url = "https://api.bilibili.com/x/v2/reply/del"
        header = {
            "cookie": "buvid3=63F2A07D-B1B2-5827-69B6-A85425C0BFC447917infoc; b_nut=1712821447; _uuid=BE5A3EC6-C910A-19AC-B5E7-73F6A9F10894A48359infoc; buvid4=1E201E00-65BC-BB72-D7C5-33C0DDE6CD3348900-024041107-VEkFsVIYhyuHFNlQUcADvw%3D%3D; rpdid=|(mmRl~uRu)0J'u~uk)kuRRm; DedeUserID=693537580; DedeUserID__ckMd5=c6c6c4798be9b9b3; buvid_fp_plain=undefined; enable_web_push=DISABLE; FEED_LIVE_VERSION=V_DYN_LIVING_UP; header_theme_version=CLOSE; is-2022-channel=1; hit-dyn-v2=1; LIVE_BUVID=AUTO4217132695647997; PVID=2; dy_spec_agreed=1; blackside_state=0; CURRENT_BLACKGAP=0; CURRENT_QUALITY=127; fingerprint=36cc6340c61e4376f0def49a1b42e8c2; home_feed_column=5; browser_resolution=1920-925; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQ0MjI1MTIsImlhdCI6MTczNDE2MzI1MiwicGx0IjotMX0.q1MCb-OkbNg8xR4J4qWftMKamnWxDcE1P-BF-2EJvcY; bili_ticket_expires=1734422452; SESSDATA=e2367de6%2C1749722023%2Ced929%2Ac2CjB6kCQJf82TkJQu889xqN-c0iK5BFeyuyPApHddrw0utezae3_1dEshC-WWFphetvgSVmoyM0JmeFdZMmpoY3JDeVBBX2xXZTBRX3RZQlcyemJ1WWI4U3EwSUNQVDgySnlWVGJjTG90VkI5TTJocTMwLWdjRWtkQ0tzQnFPNkkzRDJGNDVMUHlRIIEC; bili_jct=af0210fda7da18a136f29acb4fbf1414; b_lsid=4FA104892_193CA1B6EF0; bsource=search_bing; sid=6ncetye6; bp_t_offset_693537580=1011152300682510336; CURRENT_FNVAL=4048; buvid_fp=36cc6340c61e4376f0def49a1b42e8c2",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
        }
        response = requests.post(url=url, data=data, headers=header)
        if response.status_code == 200:
            print("删除评论成功")
        else:
            print("删除评论失败")
    try:
        rpids = get_rp_id()
        for rpid in rpids:
            del_comment(rpid)
    except:
        pass

def compete(last_card,step):
    if last_card == 0:
        return True
    if last_card[0]!= step[0]:
        return False
    if last_card[0]==step[0]:
        #进行下一步比较
        a = last_card.split(" ")[1]
        b = step.split(" ")[1]
        if a>b:
            return False
        else:
            return True

# cards,dirs = find_card()
# turn_cards,tmp_card =parse_card(cards,"过 5 ")
# dirs["player_1"] = turn_cards
# dirs["current_cards"] = eval(tmp_card)
# # print(get_last_step(dirs))
# # comment(str(dirs))
# print(dirs)


# parse_card(cards,"对 10 ")
# parse_card(cards,"三带一 5 + 3")
# parse_card(cards,"三带二 5 + 6 ")
# parse_card(cards,"顺子 3 ~ 7 ")
# parse_card(cards,"连对 3 ~ 7 ")
# parse_card(cards,"飞机 2 3 ~ 5 6 ")
# parse_card(cards,"炸弹 5")
# parse_card(cards,"王炸")

import time
while 1:
    try:
        card,dirs = find_card()
        if dirs["current_player"] == 1:
            print("是你的回合，请出牌：")
            a = 0
            if dirs["last_player"] == dirs["current_player"]:
                #我的回合开始，出牌
                dirs["current_cards"] = []
                a=1

            print(dirs["player_1"])
            print(get_last_step(dirs))
            step = input("请输入出牌：\n")

            if step == "过":
                dirs["current_player"] = 2
                clear()
                comment(str(dirs))
            #比较
            if a==1:
                turn_cards, tmp_card = parse_card(card, step)
                dirs["player_1"] = turn_cards
                dirs["current_player"] = 2
                dirs["current_cards"] = eval(tmp_card)
                dirs["last_player"] = 1
                clear()
                comment(str(dirs))
            if a==0:
                last_card = get_last_step(dirs)
                print(last_card)
                if compete(last_card,step) :
                    turn_cards,tmp_card =parse_card(card,step)
                    dirs["player_1"] = turn_cards
                    dirs["current_player"] = 2
                    dirs["current_cards"] = eval(tmp_card)
                    dirs["last_player"] = 1
                    clear()
                    comment(str(dirs))
                else:
                    print("出牌不符合规则，请重新出牌")
    except:
        time.sleep(1)
        pass