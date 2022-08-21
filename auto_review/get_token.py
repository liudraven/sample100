# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/5/19
# aim: 

# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=' \
       'client_credentials&' \
       'client_id=Fzp1ontAPGsgpuVShg2CToDI&' \
       'client_secret=7xp2xmRt2zvR4DA1lcbaFEQivXWHWoYF'
response = requests.get(host)
if response:
    print(response.json()['access_token'])

token = '24.705d2072ee1bbc201f1418863efdc918.2592000.1655562676.282335-26275249'

