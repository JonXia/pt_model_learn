import requests
import json
import chardet
import re
from pprint import pprint


######################
# xml形式的文件爬取失效
# 用接口获取
######################
# 1.根据bv请求得到cid
def get_cid(bv):
    cids = []
    url = 'https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp'.format(bv)
    res = requests.get(url).text
    json_dict = json.loads(res)
    pprint(json_dict)
    for x in json_dict["data"]:
        cids.append(x["cid"])
    return cids
 

# 2.根据cid请求弹幕，解析弹幕得到最终的数据
def get_data(cid):
    final_url = "https://api.bilibili.com/x/v1/dm/list.so?oid=" + str(cid)
    final_res = requests.get(final_url)
    final_res.encoding = chardet.detect(final_res.content)['encoding']
    final_res = final_res.text
    pattern = re.compile('<d.*?>(.*?)</d>')
    data = pattern.findall(final_res)
    return data
 

# 3.保存弹幕列表
def save_to_file(data, file):
    with open(file+".txt", mode="w", encoding="utf-8") as f:
        for i in data:
            f.write(i)
            f.write("\n")
 
 
bv = "BV1P4411F77q"
cids = get_cid(bv)
for cid in cids:
    data = get_data(cid)
    name = "{}_{}".format(bv, cid)
    save_to_file(data, name)

