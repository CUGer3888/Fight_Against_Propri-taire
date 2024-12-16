import random
import requests  # 发送请求
import re

# 3~13 :3~a 14:2 15:小王 16:大王

cards = []
for i in range(3, 16):
    for ii in range(4):
        cards.append(i)
cards.append(16)
cards.append(17)

plarer_1 = []
plarer_2 = []
plarer_3 = []
random.shuffle(cards)
print(len(cards))
for i in range(54):
    if i % 3 == 0:
        plarer_1.append(cards[i])
    elif i % 3 == 1:
        plarer_2.append(cards[i])
    else:
        plarer_3.append(cards[i])
print(plarer_1)
print(plarer_2)
print(plarer_3)
plarer_1.sort()
plarer_2.sort()
plarer_3.sort()
# 向服务器发送信息，包括 牌和玩家信息
data_dir = {
    "if_start": 0,  # 判断是否开始
    "player_1": plarer_1,
    "player_2": plarer_2,
    "player_3": plarer_3,
    "current_player": 1,  # 当前玩家
    "current_cards": [],  # 当前出牌
    "last_player": 1,  # 上一个出牌的玩家
}

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
def get_rp_id():
    url = "https://api.bilibili.com/x/v2/reply/wbi/main?oid=1011139183900622865&type=17&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=1044f149e9f46fa3bbb64d0fc3a6531f&wts=1734268044"
    header = {
            "cookie": "buvid3=63F2A07D-B1B2-5827-69B6-A85425C0BFC447917infoc; b_nut=1712821447; _uuid=BE5A3EC6-C910A-19AC-B5E7-73F6A9F10894A48359infoc; buvid4=1E201E00-65BC-BB72-D7C5-33C0DDE6CD3348900-024041107-VEkFsVIYhyuHFNlQUcADvw%3D%3D; rpdid=|(mmRl~uRu)0J'u~uk)kuRRm; DedeUserID=693537580; DedeUserID__ckMd5=c6c6c4798be9b9b3; buvid_fp_plain=undefined; enable_web_push=DISABLE; FEED_LIVE_VERSION=V_DYN_LIVING_UP; header_theme_version=CLOSE; is-2022-channel=1; hit-dyn-v2=1; LIVE_BUVID=AUTO4217132695647997; PVID=2; dy_spec_agreed=1; blackside_state=0; CURRENT_BLACKGAP=0; CURRENT_QUALITY=127; fingerprint=36cc6340c61e4376f0def49a1b42e8c2; home_feed_column=5; browser_resolution=1920-925; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQ0MjI1MTIsImlhdCI6MTczNDE2MzI1MiwicGx0IjotMX0.q1MCb-OkbNg8xR4J4qWftMKamnWxDcE1P-BF-2EJvcY; bili_ticket_expires=1734422452; SESSDATA=e2367de6%2C1749722023%2Ced929%2Ac2CjB6kCQJf82TkJQu889xqN-c0iK5BFeyuyPApHddrw0utezae3_1dEshC-WWFphetvgSVmoyM0JmeFdZMmpoY3JDeVBBX2xXZTBRX3RZQlcyemJ1WWI4U3EwSUNQVDgySnlWVGJjTG90VkI5TTJocTMwLWdjRWtkQ0tzQnFPNkkzRDJGNDVMUHlRIIEC; bili_jct=af0210fda7da18a136f29acb4fbf1414; b_lsid=4FA104892_193CA1B6EF0; bsource=search_bing; sid=6ncetye6; bp_t_offset_693537580=1011152300682510336; CURRENT_FNVAL=4048; buvid_fp=36cc6340c61e4376f0def49a1b42e8c2",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
        }
    response = requests.get(url=url, headers=header)
    rpid = re.findall(r'"rpid":(\d+)', response.text)
    return rpid

def clear():
    try:
        rpids = get_rp_id()
        for rpid in rpids:
            del_comment(rpid)
    except:
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
        "ordering": "heat",
        "jsonp": "jsonp",
    }
    header = {
        "cookie": "buvid3=63F2A07D-B1B2-5827-69B6-A85425C0BFC447917infoc; b_nut=1712821447; _uuid=BE5A3EC6-C910A-19AC-B5E7-73F6A9F10894A48359infoc; buvid4=1E201E00-65BC-BB72-D7C5-33C0DDE6CD3348900-024041107-VEkFsVIYhyuHFNlQUcADvw%3D%3D; rpdid=|(mmRl~uRu)0J'u~uk)kuRRm; DedeUserID=693537580; DedeUserID__ckMd5=c6c6c4798be9b9b3; buvid_fp_plain=undefined; enable_web_push=DISABLE; FEED_LIVE_VERSION=V_DYN_LIVING_UP; header_theme_version=CLOSE; is-2022-channel=1; hit-dyn-v2=1; LIVE_BUVID=AUTO4217132695647997; PVID=2; dy_spec_agreed=1; blackside_state=0; CURRENT_BLACKGAP=0; CURRENT_QUALITY=127; fingerprint=36cc6340c61e4376f0def49a1b42e8c2; home_feed_column=5; browser_resolution=1920-925; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQ0MjI1MTIsImlhdCI6MTczNDE2MzI1MiwicGx0IjotMX0.q1MCb-OkbNg8xR4J4qWftMKamnWxDcE1P-BF-2EJvcY; bili_ticket_expires=1734422452; SESSDATA=e2367de6%2C1749722023%2Ced929%2Ac2CjB6kCQJf82TkJQu889xqN-c0iK5BFeyuyPApHddrw0utezae3_1dEshC-WWFphetvgSVmoyM0JmeFdZMmpoY3JDeVBBX2xXZTBRX3RZQlcyemJ1WWI4U3EwSUNQVDgySnlWVGJjTG90VkI5TTJocTMwLWdjRWtkQ0tzQnFPNkkzRDJGNDVMUHlRIIEC; bili_jct=af0210fda7da18a136f29acb4fbf1414; bp_t_offset_693537580=1010989409752842240; b_lsid=4FA104892_193CA1B6EF0; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; bsource=search_bing; buvid_fp=36cc6340c61e4376f0def49a1b42e8c2; sid=6ncetye6; CURRENT_FNVAL=4048",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }
    response = requests.post(url=url, data=data, headers=header)
    if response.status_code == 200:
        print("评论成功")
    else:
        print("评论失败")

clear()
data = ''
data += str(data_dir)
print(data)
comment(data)
