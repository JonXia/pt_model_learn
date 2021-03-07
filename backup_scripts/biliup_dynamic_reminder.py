import requests  
import json
import time

uid = 525952604 # uid
url = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid="+str(uid)+"&need_top=1"
headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
latest_id = 0 #动态id

while(True):
    try:
        dynamic_json = ""
        response = requests.get(url=url, headers=headers)
        response.encoding = 'utf-8'
        dict_str = json.loads(response.text)                #转换成json格式
        card = json.loads(dict_str['data']['cards'][0]['card'])
        desc = dict_str['data']['cards'][0]['desc']
        if(desc['bvid'] != None):
            # TODO：提醒更新
            print("更新视频啦")

        time_array = time.localtime(card['ctime'])
        formatted = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        print(card['title'], formatted, card['short_link'], "更新：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(1800)
        
    except Exception as e:
        dynamic_id_str = desc["dynamic_id_str"]
        if(latest_id != 0 and latest_id != dynamic_id_str):
            latest_id = dynamic_id_str
            # TODO：提醒更新
            print('更新动态啦')
        
        # 时间
        time_array = time.localtime(card['item']['timestamp'])
        formatted = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        # 动态内容
        content = card['item']['content']
        print(formatted, content, "更新：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        
        if(desc['type'] == 2):
            description = card['item']['description']
            img_url = card['item']['pictures']['img_src']
            upload_time = card['item']['upload_time']

            time_array = time.localtime(card['item']['upload_time'])
            formatted = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
            print(formatted, description, img_url, "更新：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            
        time.sleep(1800)