#
import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver import Chrome, ChromeOptions, FirefoxOptions
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

options = FirefoxOptions()
options.add_argument("--headless")  
browser = webdriver.Firefox(options=options)
lt_url_front = 'http://www.chinaunicombidding.cn/bidInformation'
browser.get(lt_url_front)
time.sleep(6)
data00 = browser.page_source
f = open('1.html','w')
f.write(data00)
f.close()

soup = BeautifulSoup(data00, 'lxml')
l_one_tender = []
l00 = soup.find_all(attrs={"class":"ant-pro-list-row-card"})#卡片
l_list = []

for x in l00:
    l01 = re.findall('>.*?<',str(x))
    l02 = [x for x in l01 if x !='><']
    l_list.append(l02)

for x in l_list:
    if not re.findall('发布日期',str(x)):
        l_time=''
    if not re.findall('招标编号',str(x)):
        l_id=''
    if not re.findall('项目类型',str(x)):
        l_type=''

    l_name_type=re.sub('[<>]','',x[0])
    l_name=re.sub('[<>]','',x[1])
    l_tenderee=re.sub('[<>]','',x[2])

    for y in x[3:]:
        if re.findall('发布日期', str(y)):
            l_time=re.sub('[<>]','',y)
        if re.findall('招标编号', str(y)):
            l_id=re.sub('[<>]','',y)
        if re.findall('项目类型', str(y)):
            l_type=re.sub('[<>]','',y)
            
    l_one_tender.append([l_name_type,l_name,l_tenderee,l_time,l_id,l_type])

today = datetime.today().date()
yesterday = today - timedelta(days=1)
print('1已完成')

for i in range(2,100):
    button = browser.find_element(By.XPATH, "//li[@title='"+str(i)+"']")
    button.click()
    time.sleep(6)
    data00 = browser.page_source
    soup = BeautifulSoup(data00, 'lxml')
    l00 = soup.find_all(attrs={"class": "ant-pro-list-row-card"})  # 卡片
    l_list = []
    
    for x in l00:
        l01 = re.findall('>.*?<', str(x))
        l02 = [x for x in l01 if x != '><']
        l_list.append(l02)
        
    for x in l_list:
        if not re.findall('发布日期', str(x)):
            l_time = ''
        if not re.findall('招标编号', str(x)):
            l_id = ''
        if not re.findall('项目类型', str(x)):
            l_type = ''
        l_name_type = re.sub('[<>]', '', x[0])
        l_name = re.sub('[<>]', '', x[1])
        l_tenderee = re.sub('[<>]', '', x[2])
        
        for y in x[3:]:
            if re.findall('发布日期', str(y)):
                l_time = re.sub('[<>]', '', y)
            if re.findall('招标编号', str(y)):
                l_id = re.sub('[<>]', '', y)
            if re.findall('项目类型', str(y)):
                l_type = re.sub('[<>]', '', y)
                
        l_one_tender.append([l_name_type, l_name, l_tenderee, l_time, l_id, l_type])
        
    print(str(i)+'已完成')
    
    if not re.findall(str(today),str(l_one_tender[-1])):
        print('break')
        break

df01 = pd.DataFrame()
df01['公告类型'] = [d[0] for d in l_one_tender]
df01['公告名称'] = [d[1] for d in l_one_tender]
df01['招标人'] = [d[2] for d in l_one_tender]
df01['发布日期'] = [d[3] for d in l_one_tender]
df01['招标编号'] = [d[4] for d in l_one_tender]
df01['项目类型'] = [d[5] for d in l_one_tender]

df02 = df01[df01['发布日期'].str.contains(str(today))]
print(df02)

key_words =['政企','语音','客服','客户服务','外呼','呼叫','微信','公众号','企微','数据分析','投诉','机器人','运营','智能','媒体','招募','入围','软件开发','合作伙伴','创新业务','渠道','存量','工单','大数据','营销','维系','维护','质检','上云','AI','APP','IT','IVR','5G','DICT','BSS','10000']
str_kw = "|".join(key_words)

df03 = df02[df02['公告名称'].str.contains(str_kw)]
df03['命中关键词']=df03['公告名称'].apply(lambda x:re.findall(str_kw,x))
df03.to_csv(str(today)+'联通招标项目清单.csv',index=0)

# l00 = soup.find_all(attrs={'class':"ant-tag ant-tag-has-color",'style':"background-color: rgb(103, 122, 251); display: flex; align-items: center; justify-content: center; width: 108px;"})#中选候选人公示
# for x in l00:
#     print(x)
# l00 = soup.find_all(attrs={'class':"ant-tag ant-tag-has-color",'style':'background-color: rgb(255, 168, 0); display: flex; align-items: center; justify-content: center; width: 108px;'})#招标采购公告
# for x in l00:
#     print(x)
# l00 = soup.find_all(attrs={"style":"font-size: 16px; font-weight: 600; padding: 0px;"})#招标公告名称
# for x in l00:
#     print(x)
# l00 = soup.find_all(attrs={"style":"font-size: 14px; color: rgb(102, 102, 102); padding: 5px 0px;"})#招标人
# for x in l00:
#     print(x)
# l00 = soup.find_all(attrs={"style":"font-size: 14px; color: rgb(153, 153, 153); padding: 5px 0px;"})#发布日期
# for x in l00:
#     print(x)
# l00 = soup.find_all(attrs={"style":"padding: 5px 0px 0px;"})#招标编号/
# for x in l00:
#     print(x)
