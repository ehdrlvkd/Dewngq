from os import access
from urllib import response
import requests
import json
import appkey
import pandas as pd

track_filepath = 'C:\\Dewngq\\Dewngq\\metadata\\track.json'
with open(track_filepath,'r',encoding='UTF-8') as f:
        track_data = json.load(f)

slack_token = appkey.slack_token

def post_message (token, channel, text):

    response = requests.post("https://slack.com/api/chat.postMessage",
    headers = {"Authorization" : "Bearer " + token},
    data = {"channel" : channel , "text" : text}
    )

    print(response)

nexon_appkey = appkey.appkey

# nickname = input("닉네임은 ? ")
nickname = 'mystic벤츠'

# request 시에 필수로 headers 사용
headers={'Authorization':nexon_appkey}

AppURL = f'https://api.nexon.co.kr/kart/v1.0/users/nickname/{nickname}'



req=requests.get(AppURL,headers=headers)
# req=requests.get(matchURL,headers=headers)

if req.status_code == 200:

    match_data = req.json()
    access_id = match_data['accessId']
    start_date = ''
    end_date = ''
    offset = ''
    limit = ''
    match_types = ''
    match_map_list = []

    matchURL = f'https://api.nexon.co.kr/kart/v1.0/users/{access_id}/matches?start_date={start_date}&end_date={end_date} &offset={offset}&limit={limit}&match_types={match_types}'
    match_req = requests.get(matchURL,headers=headers)

    if match_req.status_code == 200 :
        match_detail_date = match_req.json()
        count = 0 
        for i in range(0,len(match_detail_date['matches'])):
            for j in range(0,len(match_detail_date['matches'][i]['matches'])):
                match_map_list.append(match_detail_date['matches'][i]['matches'][j]['trackId'])

        for i in range(0,len(track_data)):
            for j in range(0,len(match_map_list)):
                if str(match_map_list[j]) == str(track_data[i]['id']):
                    print(track_data[i]['name'])

else:
    print(req.status_code)



